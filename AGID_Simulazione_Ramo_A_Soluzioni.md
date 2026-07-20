# Soluzioni — Simulazione Ramo A: Standard & Interoperabilità

> Risposte modello alla [simulazione Ramo A](AGID_Simulazione_Ramo_A.md), redatte per coprire tutte le voci della griglia di autocorrezione. Usale per confrontarti dopo aver scritto la tua risposta, non al posto dell'esercizio a tempo.

---

## Quesito sintetico — OAuth 2.0

OAuth 2.0 (RFC 6749) è un **framework di autorizzazione**, non di autenticazione: consente a un'applicazione client di ottenere un accesso limitato (scope) a una risorsa protetta per conto di un utente, senza che il client conosca o gestisca le credenziali dell'utente stesso.

**Ruoli.** Il modello definisce quattro attori: il *resource owner* (l'utente che possiede la risorsa), il *client* (l'applicazione che richiede accesso), l'*authorization server* (che autentica il resource owner e rilascia i token) e il *resource server* (che espone l'API protetta e accetta l'access token).

**Flusso Authorization Code + PKCE.** Il client reindirizza il browser dell'utente all'endpoint `/authorize` dell'authorization server; l'utente si autentica e presta il consenso agli scope richiesti; l'authorization server reindirizza il client a un `redirect_uri` con un *authorization code* monouso; il client scambia lato back-channel questo codice, insieme al `code_verifier` (il segreto che ha generato il `code_challenge` inviato nella richiesta iniziale), con l'`access_token` presso l'endpoint `/token`.

PKCE (Proof Key for Code Exchange, RFC 7636) è ormai richiesto anche per i client *confidential* — non solo per i client pubblici (SPA, mobile) per cui nacque — perché protegge dal furto dell'authorization code: se il codice viene intercettato (es. tramite un redirect_uri malevolo o un log applicativo), un attaccante non può scambiarlo con un token senza conoscere il `code_verifier` originario, che non transita mai in chiaro nella fase di redirect.

È importante distinguere l'**access token** (oggetto di OAuth 2.0, dice "cosa può fare il client", opaco o JWT con scope) dall'**ID token** (oggetto di OpenID Connect, l'estensione di autenticazione costruita sopra OAuth 2.0, dice "chi è l'utente" tramite claim firmati JWT). SPID/CIE, ad esempio, utilizzano proprio OpenID Connect per la federazione dell'identità digitale, mentre l'autorizzazione verso le API resta gestita con i soli meccanismi OAuth 2.0.

**Perché mTLS in affiancamento nel ModI.** Le Linee Guida AGID sulla sicurezza delle API richiedono che, nelle interazioni sistema-sistema della PA, OAuth 2.0 sia affiancato da mTLS: OAuth prova **cosa può fare** il chiamante (lo scope autorizzato dal token), ma non garantisce **chi è** il sistema che lo presenta — un access token di tipo bearer, se rubato o intercettato, è utilizzabile da chiunque lo possieda (fino alla scadenza). mTLS autentica invece l'identità del sistema chiamante a livello di trasporto tramite certificato X.509, realizzando una difesa in profondità: anche se un token bearer venisse sottratto, non potrebbe essere presentato con successo senza il certificato client legittimo.

**Rischio e mitigazione:** il rischio principale resta il furto/replay di un token bearer (es. tramite log applicativi non sanificati o un endpoint intermedio compromesso); le mitigazioni tipiche sono scope minimi (least privilege), TTL breve dell'access token, refresh token con rotazione, ed endpoint di *introspection*/revoca per invalidare un token compromesso prima della sua naturale scadenza.

---

## Quesito sintetico — mTLS (Mutual TLS)

Nel TLS standard solo il server presenta un certificato X.509 al client, che lo verifica per autenticare il server e stabilire un canale cifrato; in **Mutual TLS (mTLS)** anche il **client** presenta un proprio certificato X.509, così che l'autenticazione avvenga in entrambe le direzioni.

**Handshake esteso.** Rispetto al TLS handshake standard, il server invia un messaggio `CertificateRequest` dopo il proprio `Certificate`; il client risponde inviando il proprio `Certificate` e un messaggio `CertificateVerify`, in cui firma con la propria chiave privata un hash dei messaggi di handshake scambiati fino a quel momento, dimostrando così il possesso della chiave privata associata al certificato presentato.

**Verifiche lato server.** Il server, ricevuto il certificato client, verifica: la catena di certificazione fino a una CA presente nel proprio truststore; la validità temporale del certificato (not-before/not-after); lo stato di revoca tramite CRL o OCSP.

Un punto chiave è che questa autenticazione avviene interamente **a livello di trasporto** (durante l'handshake TLS), prima che qualunque richiesta applicativa (HTTP) venga inviata: se il client non supera la verifica del certificato, la connessione non si stabilisce affatto.

**Perché serve nel Modello di Interoperabilità.** Nelle interazioni ModI non c'è un utente umano che si autentica, ma un sistema di una PA che ne chiama un altro: mTLS garantisce che la chiamata provenga effettivamente dall'ente accreditato, ancorando l'identità del chiamante a un certificato emesso e tracciato in fase di accreditamento, indipendentemente da qualsiasi token applicativo.

**Complementarità con OAuth 2.0.** I due meccanismi rispondono a domande diverse e non sono alternativi: mTLS prova **"chi sei"** (identità del sistema chiamante, a livello di trasporto), OAuth 2.0 prova **"cosa puoi fare"** (lo scope autorizzato, a livello applicativo). Nel ModI sono richiesti congiuntamente proprio per coprire entrambe le dimensioni.

**Trade-off operativi.** L'adozione di mTLS comporta oneri concreti: il ciclo di vita e la rotazione periodica dei certificati client (rinnovo, distribuzione sicura delle chiavi private) sono un onere operativo non banale su larga scala; la revoca tramite CRL/OCSP è tipicamente più lenta e meno "in tempo reale" di una revoca di token OAuth; infine, se la terminazione TLS avviene su un load balancer o reverse proxy, occorre progettare con attenzione come l'identità del certificato client venga propagata (es. header fidati) all'applicazione a valle, senza introdurre un punto di spoofing.

---

## Quesito sintetico — PDND (Piattaforma Digitale Nazionale Dati)

PDND non è un data lake centrale: è un **control-plane/broker di fiducia**. I dati non transitano mai attraverso PDND — la chiamata con i dati veri e propri avviene direttamente, punto-punto, tra l'ente fruitore e l'ente erogatore; PDND si limita a orchestrare fiducia, scoperta e autorizzazione dell'interazione.

**Attori.** Il modello coinvolge tre soggetti: l'**ente erogatore** (che espone un e-service con i propri dati), l'**ente fruitore** (che consuma il dato) e **PDND** stessa, come infrastruttura abilitante.

**Catalogo E-Service.** È il punto di pubblicazione e scoperta: ogni ente erogatore pubblica nel catalogo gli e-service che espone, con le relative interfacce tecniche, rendendoli individuabili dagli enti fruitori.

**Finalità.** Il fruitore, per attivare l'accesso a un e-service, deve dichiarare la **finalità** per cui richiede il dato: questo attua il principio di limitazione della finalità (purpose limitation) e la privacy by design fin dal disegno dell'interazione.

**Accordo di fruizione.** È la sottoscrizione attiva tra fruitore ed erogatore, legata a una specifica finalità dichiarata: solo dopo la sua stipula il fruitore può richiedere l'accesso operativo all'e-service.

**Voucher.** È un token a breve durata rilasciato da PDND dopo aver verificato una *client assertion* JWT, firmata dal fruitore con la propria chiave privata — uno schema coerente con RFC 7523 (JWT Bearer Grant): il fruitore dimostra così la propria identità a PDND, che rilascia il voucher da presentare all'ente erogatore per l'accesso effettivo all'e-service.

**Once Only.** Il modello realizza concretamente il principio Once Only previsto dal CAD (art. 18, art. 50): nessun dato viene duplicato in un archivio centrale; quando un ente ha già un dato in possesso (o disponibile presso un'altra PA), la PA che ne ha bisogno lo richiede in tempo reale tramite PDND, invece di richiederlo nuovamente al cittadino.

---

## Caso gestionale

*Metodo (4 mosse): (1) inquadramento normativo, (2) metodo progettuale, (3) soluzione tecnica, (4) rischio & budget.*

**Contesto.** Un Ministero e un Comune capoluogo devono far dialogare i rispettivi sistemi per erogare un contributo economico online, recuperando dati reddituali già in possesso del Ministero, senza richiederli nuovamente al cittadino. Il Comune non ha esperienza pregressa di integrazione via PDND.

### (a) Modello di interoperabilità

L'integrazione punto-punto ad hoc (es. un webservice dedicato tra i due enti, con credenziali gestite fuori standard) va scartata: crea un accoppiamento stretto e non riusabile, nessuna standardizzazione dei controlli di sicurezza, tracciabilità debole e un costo di manutenzione che cresce linearmente col numero di integrazioni bilaterali.

La scelta corretta è il modello **PDND**: il Ministero pubblica nel **Catalogo E-Service** l'e-service che espone i dati reddituali; il Comune, come ente fruitore, individua l'e-service nel catalogo e sottoscrive un **accordo di fruizione** legato alla specifica finalità (erogazione del contributo). Questo garantisce minore accoppiamento (l'integrazione è mediata da uno standard nazionale, non da un contratto bilaterale ad hoc), standardizzazione tecnica (stesso pattern di autenticazione/autorizzazione per tutte le integrazioni PA-PA) e tracciabilità centralizzata degli accessi.

### (b) Sicurezza dello scambio

Coerentemente con le Linee Guida AGID sulla sicurezza delle API (v. `AGID/pdf/05`), lo scambio deve prevedere tre livelli distinti e complementari:
- **Autenticazione del sistema chiamante**: mTLS con certificato X.509, per garantire che la chiamata provenga effettivamente dal sistema accreditato del Comune (identità a livello di trasporto);
- **Autorizzazione**: OAuth 2.0 tramite il **voucher PDND**, rilasciato dopo verifica di una client assertion JWT (RFC 7523), che attesta lo scope autorizzato dall'accordo di fruizione;
- **Cifratura in transito**: TLS 1.2/1.3 su tutto il canale, sia per l'handshake mTLS sia per il payload applicativo.

Questi tre meccanismi realizzano la difesa in profondità già vista nei quesiti sintetici: mTLS risponde a "chi sei", OAuth/voucher a "cosa puoi fare", TLS alla confidenzialità/integrità del dato in transito.

### (c) Once Only e privacy

La soluzione realizza il principio Once Only perché il Comune non richiede più il dato reddituale al cittadino: lo recupera in tempo reale dal Ministero al momento dell'istruttoria, tramite l'accordo di fruizione attivato su PDND. Sul piano privacy vanno rispettate: la **finalità dichiarata** nell'accordo (il dato reddituale è richiesto esclusivamente per il calcolo del contributo, non riusabile per altri scopi senza un nuovo accordo) e la **minimizzazione**, limitando la richiesta ai soli campi effettivamente necessari al calcolo (es. reddito imponibile, non l'intera dichiarazione).

### (d) Rischi e mitigazioni

- **Indisponibilità del sistema erogatore** (il Ministero): va previsto un meccanismo di timeout/fallback e un piano di gestione del procedimento in caso di mancata risposta entro SLA (es. sospensione dei termini, non blocco totale del servizio al cittadino);
- **Ciclo di vita dei certificati mTLS**: il Comune deve presidiare rinnovo e rotazione dei certificati client, per evitare interruzioni impreviste del servizio per scadenza certificato;
- **Revoca degli accessi**: gestione del TTL breve del voucher e possibilità di revoca dell'accordo di fruizione in caso di cessata necessità o incidente di sicurezza;
- **Organizzativo**: mancanza di esperienza pregressa del Comune con PDND → mitigazione tramite formazione tecnica del team e, se disponibile, riuso di soluzioni/e-service già collaudati da altri enti (principio di riuso del Piano Triennale).

**Criticità residue.** Il Comune resta comunque dipendente dai tempi di risposta/disponibilità del sistema del Ministero e dalla qualità del dato reddituale esposto (se non aggiornato in tempo reale, potrebbe non riflettere variazioni recenti di reddito).
