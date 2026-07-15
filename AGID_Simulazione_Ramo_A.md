# Simulazione — Ramo A: Standard & Interoperabilità
### Concorso AGID-01 · Materie 1, 2 del bando (art. 7)

> **Formato.** Come da bando, la prova reale è composta da uno o più quesiti a risposta sintetica e uno o più casi gestionali, in 4 ore complessive su tutte le materie. Questa è una simulazione **parziale**, mirata al solo Ramo A — usala come allenamento a tempo, non come prova completa.
>
> **Fonti di riferimento:** [Sintesi_Normazione_Interoperabilita.md](Sintesi_Normazione_Interoperabilita.md), `AGID/Pubblicazioni_e_Linee_Guida_AGID.md` §1-2, `AGID/pdf/03-06` e `21`.
>
> Vedi anche la [mappa mentale del concorso](Mappa_Mentale_AGID.html) — ramo A.

---

## Quesito sintetico — OAuth 2.0
### Materie 1 · 2 · ⏱ 15'

> Il candidato descriva sinteticamente il framework OAuth 2.0, i ruoli coinvolti e il flusso *Authorization Code* con PKCE, illustrando perché le Linee Guida AGID sulla sicurezza delle API richiedono di affiancarlo a **mTLS** nelle interazioni tra sistemi della Pubblica Amministrazione.

### Griglia di autocorrezione

| Punto da toccare | ✓ |
|---|---|
| Definisce OAuth 2.0 come framework di **autorizzazione**, non autenticazione (RFC 6749) | ☐ |
| Elenca i 4 ruoli: resource owner, client, authorization server, resource server | ☐ |
| Descrive il flusso Authorization Code + PKCE: redirect a `/authorize`, consenso, `authorization code`, scambio con `code_verifier` per l'`access_token` | ☐ |
| Spiega perché PKCE è ormai richiesto anche per client confidential (protezione dal furto del code) | ☐ |
| Distingue **access token** (OAuth 2.0, "cosa può fare il client") da **ID token** (OpenID Connect, "chi è l'utente"), citando OIDC in SPID come caso reale | ☐ |
| Collega al ModI: OAuth 2.0 prova lo scope autorizzato, **mTLS/X.509** prova l'identità del sistema PA chiamante → difesa in profondità contro il furto/replay di un token bearer | ☐ |
| Cita almeno un rischio e la relativa mitigazione (token bearer rubabile → scope minimi, TTL breve, revoca/introspection) | ☐ |

**Soglia orientativa:** 5/7 voci toccate = risposta solida per una domanda sintetica di questo tipo.

---

## Quesito sintetico — mTLS (Mutual TLS)
### Materie 1 · 2 · ⏱ 15'

> Il candidato descriva il funzionamento del Mutual TLS e in cosa differisce da un handshake TLS standard, spiegando perché le Linee Guida AGID sulla sicurezza delle API lo prescrivono per l'autenticazione server-to-server nel Modello di Interoperabilità, e come si combina con OAuth 2.0.

### Griglia di autocorrezione

| Punto da toccare | ✓ |
|---|---|
| Spiega che nel TLS standard solo il server presenta un certificato, mentre in mTLS anche il **client** presenta un certificato X.509 | ☐ |
| Descrive l'handshake esteso: `CertificateRequest` del server → `Certificate` del client → `CertificateVerify` (firma con la chiave privata del client) | ☐ |
| Indica le verifiche fatte dal server sul certificato client: catena fino a una CA/truststore fidato, validità temporale, stato di revoca (CRL/OCSP) | ☐ |
| Chiarisce che l'autenticazione avviene **a livello di trasporto**, prima che parta qualunque richiesta applicativa | ☐ |
| Spiega perché serve nel ModI: non c'è un utente umano, è un sistema PA che chiama un altro sistema PA — mTLS garantisce che la chiamata provenga dall'ente accreditato | ☐ |
| Distingue i ruoli complementari: mTLS prova **"chi sei"** (identità del sistema), OAuth 2.0 prova **"cosa puoi fare"** (scope) — non sono alternativi | ☐ |
| Cita almeno un trade-off operativo (ciclo di vita/rotazione dei certificati client, revoca CRL/OCSP più lenta di una token revocation, gestione della terminazione TLS dietro un load balancer) | ☐ |

**Soglia orientativa:** 5/7 voci toccate = risposta solida per una domanda sintetica di questo tipo.

---

## Quesito sintetico — PDND (Piattaforma Digitale Nazionale Dati)
### Materie 1 · 2 · ⏱ 15'

> Il candidato descriva il funzionamento di PDND, chiarendo perché non è un data lake centrale, quali sono gli attori e i concetti principali (e-service, finalità, accordo di fruizione, voucher) e come il modello realizza il principio Once Only.

### Griglia di autocorrezione

| Punto da toccare | ✓ |
|---|---|
| Chiarisce che PDND è un **control-plane/broker di fiducia**: i dati non transitano da PDND, la chiamata avviene direttamente tra fruitore ed erogatore | ☐ |
| Elenca gli attori: ente erogatore, ente fruitore, PDND | ☐ |
| Descrive il Catalogo E-Service come punto di pubblicazione/scoperta degli e-service esposti dagli enti erogatori | ☐ |
| Spiega il ruolo della **Finalità**: il fruitore dichiara il motivo dell'accesso, attuando la limitazione di finalità (privacy by design) | ☐ |
| Descrive l'**Accordo di fruizione** come sottoscrizione attiva tra fruitore ed erogatore, legata a una finalità | ☐ |
| Spiega il **Voucher**: token a breve durata rilasciato da PDND dopo aver verificato un client assertion JWT firmato dal fruitore con la propria chiave privata (schema coerente con RFC 7523) | ☐ |
| Collega il modello al principio **Once Only**: nessun dato duplicato in un archivio centrale, la PA richiede il dato in tempo reale invece di chiederlo al cittadino | ☐ |

**Soglia orientativa:** 5/7 voci toccate = risposta solida per una domanda sintetica di questo tipo.

---

*(altri quesiti sintetici sul ramo A verranno aggiunti qui in fase di ripasso)*

---

## Caso gestionale

> Due amministrazioni — un Ministero e un Comune capoluogo — devono realizzare un nuovo servizio digitale che consente al cittadino di richiedere online un contributo economico. Il servizio deve recuperare automaticamente, dal sistema del Ministero, alcuni dati reddituali già in possesso dell'amministrazione centrale, senza chiederli nuovamente al cittadino. Il Comune non ha mai integrato sistemi esterni tramite PDND ed è preoccupato sia per la sicurezza dell'integrazione sia per la conformità agli standard tecnici richiesti da AGID.
>
> Il candidato, assumendo il ruolo di responsabile ICT del Comune:
>
> **(a)** individui il modello di interoperabilità da adottare (PDND, e-service, accordo di fruizione), motivando la scelta rispetto a un'integrazione punto-punto ad hoc tra i due enti;
>
> **(b)** descriva i meccanismi di sicurezza da implementare nello scambio (autenticazione del sistema chiamante, autorizzazione, cifratura in transito), citando gli standard tecnici e le Linee Guida AGID di riferimento;
>
> **(c)** spieghi come la soluzione realizza il principio Once Only e quali garanzie di finalità/minimizzazione del dato vanno rispettate lato privacy;
>
> **(d)** individui i principali rischi tecnici e organizzativi dell'integrazione (es. indisponibilità del sistema erogatore, gestione del ciclo di vita dei certificati, revoca degli accessi) e le relative misure di mitigazione.
>
> Si motivino le scelte e si segnalino eventuali criticità residue.

### Griglia di autocorrezione — Caso gestionale

| Punto | Cosa deve comparire nella risposta | ✓ |
|---|---|---|
| (a) Modello | PDND come control-plane/broker di fiducia (non data lake); Catalogo E-Service per la scoperta dell'e-service del Ministero; accordo di fruizione legato a una finalità dichiarata; preferenza rispetto a integrazione punto-punto (minore accoppiamento, standardizzazione, tracciabilità) | ☐ |
| (b) Sicurezza | mTLS/X.509 per l'autenticazione del sistema chiamante, OAuth 2.0/voucher PDND per l'autorizzazione, TLS 1.2/1.3 per la cifratura in transito; riferimento alle Linee Guida AGID sicurezza API (`AGID/pdf/05`) | ☐ |
| (c) Once Only & privacy | Nessuna richiesta duplicata del dato reddituale al cittadino; finalità dichiarata nell'accordo di fruizione; minimizzazione (solo i dati necessari al calcolo del contributo) | ☐ |
| (d) Rischi | Indisponibilità del sistema erogatore (gestione fallback/timeout), rotazione e revoca dei certificati client, gestione del voucher (TTL breve, rinnovo), audit/logging degli accessi | ☐ |
| Metodo | La risposta segue le 4 mosse (norma → metodo → soluzione tecnica → rischio/budget) invece di elencare i fatti senza struttura | ☐ |

---

> **Come proseguire.** Scrivi la tua risposta al caso gestionale (anche solo per punti) e incollala in chat: te la correggo voce per voce sulla griglia sopra, segnalando cosa manca e cosa è già solido.
