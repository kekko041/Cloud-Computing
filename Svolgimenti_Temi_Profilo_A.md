# Svolgimenti — Prova scritta Profilo A (Esperto ICT)
### Risposte-modello ai sette temi · Banca d'Italia 2026 (sei ufficiali + un tema extra di allenamento)

> Ogni svolgimento segue la struttura attesa dalla Commissione: **impostazione del problema → sviluppo tecnico con specifiche concrete → esempi calati nel contesto Banca d'Italia/Eurosistema → conclusione con rischi residui**, secondo il metodo PEEL.

---
---

# AMBITO 1 — Computazione, software, sistemi

## Svolgimento Tema 1.1 — Architettura di un sistema di pagamento ad alta disponibilità

**Impostazione.** Un sistema di regolamento lordo in tempo reale (RTGS) per pagamenti interbancari di importo elevato è un'infrastruttura *systemic*: l'errore non è un disservizio, è un rischio per la stabilità finanziaria. Tre principi guidano quindi ogni scelta: **finalità e consistenza forte del regolamento** (un pagamento regolato è definitivo e irrevocabile), **continuità operativa quasi-continua**, **resilienza dimostrabile** ai sensi del Regolamento DORA. Questi requisiti orientano i trade-off in direzione opposta a quella di una tipica applicazione web: qui la *consistenza* prevale sulla *disponibilità eventuale*.

**(a) Architettura applicativa.** Scarto il monolite puro (non scala e ostacola il rilascio indipendente) e diffido del microservizio "estremo" per il cuore di regolamento, dove la coerenza transazionale è critica. Propongo un'architettura **a microservizi orientati agli eventi (event-driven)** con un nucleo conservativo:

- un **gateway di messaggistica** standard ISO 20022 che riceve, valida sintatticamente e autentica i messaggi di pagamento;
- servizi di **controllo (anti-duplicazione, controlli di liquidità, sanzioni/embarghi)** disaccoppiati tramite un *event backbone* (es. Apache Kafka), con messaggi **idempotenti** e ordinamento garantito per chiave;
- un **motore di regolamento** che mantiene il *ledger* come unica fonte di verità, con scritture **ACID** e finalità transazione-per-transazione;
- servizi di **reportistica e interrogazione** alimentati da repliche in sola lettura.

L'event-driven offre disaccoppiamento, scalabilità orizzontale dei controlli e tracciabilità (event sourcing), mantenendo però il regolamento centralizzato e fortemente consistente. Pattern utili: **CQRS** (separazione scrittura/lettura), **Saga** per i flussi multi-step con compensazione, **outbox transazionale** per pubblicare eventi senza perdere atomicità.

**(b) Consistenza nel sistema distribuito.** Il teorema **CAP** impone, in presenza di partizione di rete, di scegliere tra consistenza e disponibilità. Per il ledger di regolamento la scelta è netta: **CP** (consistenza + tolleranza alle partizioni). Le proprietà **ACID** garantiscono che non esistano due stati di regolamento in conflitto — condizione non negoziabile per la finalità giuridica del pagamento. I modelli **BASE** (consistenza eventuale) sono accettabili solo nei domini periferici: cruscotti, reportistica, repliche di lettura, dove un ritardo di propagazione di pochi secondi non genera rischio.

**(c) Alta disponibilità e disaster recovery.** Progetto su **due region geograficamente separate** con un terzo sito di salvaguardia, schema coerente con i requisiti di resilienza estrema (l'euro digitale, ad esempio, prevede infrastruttura distribuita su almeno tre region). Per il ledger: **active-passive con replica sincrona** sul sito secondario in zona vicina (RPO≈0) e replica asincrona sul sito remoto (protezione da disastro regionale). Per i servizi *stateless* di controllo: **active-active** multi-zona con bilanciamento. Obiettivi: **RTO** dell'ordine dei minuti, **RPO** prossimo a zero per i dati di regolamento. Procedure di *failover* testate periodicamente e *switchover* pianificati.

**(d) Osservabilità e gestione incidenti.** *Logging* strutturato e immutabile (audit trail), *distributed tracing* (OpenTelemetry) per seguire un pagamento end-to-end attraverso i microservizi, *metriche* su throughput, latenza di regolamento e tassi di errore con **SLO** espliciti. La gestione degli incidenti segue le 6 fasi del NIST IR (preparazione, identificazione, contenimento, eradicazione, recupero, lezioni apprese) e i pilastri DORA: governance del rischio ICT, *incident reporting*, *testing* della resilienza (compreso il *threat-led penetration testing*), gestione del **rischio di terze parti** (provider cloud).

**Esempio nel contesto.** L'ambiente TARGET dell'Eurosistema, di cui la Banca d'Italia è uno dei gestori tecnici, elabora quotidianamente pagamenti per controvalori enormi: un'indisponibilità prolungata avrebbe effetti sistemici. Le scelte sopra (CP sul ledger, multi-region, RPO≈0) riflettono proprio questa criticità.

**Rischi residui.** (1) **Guasti correlati**: in active-active un bug software o una configurazione errata si propaga simultaneamente — mitigazione con *canary release* e *feature flag*. (2) **Outage di region**: dipendenza da un singolo fornitore cloud → **rischio di concentrazione** che DORA impone di governare (strategie multi-cloud o exit plan). (3) **Cyber**: il sistema è bersaglio ad alto valore → difesa in profondità e Zero Trust. (4) **Rischio di liquidità intraday** se i controlli rallentano la coda di regolamento.

---

## Svolgimento Tema 1.2 — Piattaforma dati di vigilanza: relazionale vs NoSQL

**Impostazione.** Una piattaforma di analisi a supporto della vigilanza deve ingerire dati fortemente eterogenei — segnalazioni strutturate di bilancio, serie storiche, log di transazioni, documenti in testo libero — e servire analisi statistiche, controlli di qualità dei dati e modelli di rischio. Nessun singolo paradigma di storage si adatta a tutto questo: la decisione architetturale di fondo è quindi la *polyglot persistence* governata da un'architettura unificata, non un singolo database "migliore in assoluto".

**(a) Architettura end-to-end.** Propongo un'architettura **Lakehouse**, che combina il costo contenuto e la flessibilità di schema di un Data Lake con le garanzie transazionali e le prestazioni di un Data Warehouse. Un Data Warehouse puro è troppo rigido per gli input non strutturati; un Data Lake grezzo rischia di diventare un "data swamp" (pantano di dati) senza governance. Il Lakehouse, costruito su un object store con un formato tabellare aperto (es. Delta Lake o Apache Iceberg), risolve questa tensione. Livelli della pipeline:

- **Ingestione** — streaming tramite Apache Kafka per i log di transazione, caricamenti batch per le segnalazioni periodiche;
- **Storage** — un'organizzazione a *medaglioni* (medallion): *bronze* (grezzo), *silver* (ripulito/validato), *gold* (curato, pronto per l'analisi);
- **Elaborazione** — Apache Spark (e Flink per lo streaming) per le trasformazioni e il calcolo delle feature, orchestrati con Airflow/dbt;
- **Serving** — un motore di data warehouse columnare per le query analitiche, più store specializzati per i dati non tabellari.

Sulla scelta **Lambda vs Kappa**: Lambda mantiene livelli batch e speed separati (robusto ma duplica la logica); **Kappa** tratta tutto come uno stream ed è più semplice da mantenere. Per la vigilanza, dove la maggior parte delle analisi è periodica e la riproducibilità è importante, un approccio **Lambda a prevalenza batch** è pragmatico, con un percorso di streaming solo per i controlli quasi in tempo reale.

**(b) Relazionale vs NoSQL per tipo di dato.** La decisione segue la forma del dato e il pattern di accesso, guidata dal **teorema CAP**:

- *Segnalazioni di bilancio e regolamentari* → **relazionale / warehouse columnare**. Schema rigido, vincoli di integrità, join e aggregazioni complesse; qui dominano ACID e consistenza (CP).
- *Serie storiche* (tassi, dati di mercato) → **store columnare o time-series**, ottimizzato per range scan e compressione.
- *Log di transazione* (alto volume, append-only) → store **wide-column / key-value** per l'elevato throughput di scrittura; la consistenza eventuale (AP) è accettabile.
- *Documenti* (report, corrispondenza) → **document store** più un motore di ricerca/indicizzazione.
- *Reti di proprietà ed esposizione* → **database a grafo**. L'attraversamento delle relazioni (titolarità effettiva, esposizioni infragruppo) è l'ambito in cui i grafi superano i join relazionali — direttamente rilevante per l'analisi **AML e del rischio sistemico**.

Sulla modellazione: il warehouse usa **schemi a stella denormalizzati** per analisi ad alta intensità di lettura, mentre il livello operativo resta **normalizzato** per evitare anomalie di aggiornamento. La denormalizzazione scambia spazio di storage e complessità di scrittura con velocità di interrogazione.

**(c) Ottimizzazione delle query e qualità dei dati.** Leve di performance: **partizionamento** (es. per data di segnalazione), **indicizzazione**, *predicate/column pushdown*, **viste materializzate** per le aggregazioni ricorrenti, e ottimizzazione *cost-based* guidata dalle statistiche. La qualità del dato si garantisce tramite **regole di validazione** al livello silver, **deduplicazione**, riconciliazione rispetto a totali di controllo, e **data lineage** end-to-end, in modo che ogni valore sia tracciabile fino alla fonte — essenziale per un'autorità di vigilanza che deve poter difendere i propri numeri.

**(d) Requisiti non funzionali.** Scalabilità orizzontale grazie al modello disaccoppiato storage/calcolo; sicurezza tramite cifratura at-rest e in transito, controllo degli accessi granulare e audit logging; **conformità GDPR** tramite minimizzazione dei dati, limitazione delle finalità e pseudonimizzazione dei dati personali; governance tramite un catalogo dati e attività di *data stewardship*.

**Esempio nel contesto.** Una banca centrale come la Banca d'Italia è, in larga misura, un vasto sistema di basi di dati in evoluzione e interrogabili; le funzioni di vigilanza e statistiche dipendono esattamente da una piattaforma governata e multi-modello di questo tipo.

**Rischi residui.** (1) **Deriva verso il data swamp** senza una governance disciplinata. (2) **Deriva di schema/contratto** tra i sistemi sorgente e la piattaforma. (3) **Costo** di storage e calcolo su larga scala. (4) **Gap di riconciliazione** tra paradigmi diversi, che possono minare la fiducia nei dati. (5) **Rischio di re-identificazione** se la pseudonimizzazione è debole.

---

## Svolgimento Tema 1.3 — Modernizzazione cloud-native e sicurezza applicativa di una piattaforma di raccolta segnalazioni di vigilanza

**Impostazione.** Migrare una piattaforma di raccolta segnalazioni da monolite su server fisici a un'infrastruttura cloud-native comporta un cambio di paradigma non solo tecnologico ma di responsabilità: l'isolamento che prima era garantito "gratis" dalla separazione fisica delle macchine va ricostruito esplicitamente a livello di sistema operativo, rete e pipeline di sviluppo. In un contesto multi-tenant (più dipartimenti, più intermediari esterni) il rischio dominante è che un compromesso o un malfunzionamento di un tenant si propaghi agli altri: ogni scelta tecnica va quindi valutata primariamente sul criterio dell'isolamento, poi su scalabilità e velocità di rilascio.

**(a) Containerizzazione e orchestrazione.** Una macchina virtuale virtualizza l'hardware: include un intero sistema operativo guest, con un hypervisor che media l'accesso alle risorse fisiche — isolamento forte ma overhead elevato (minuti di boot, GB di immagine). Un container virtualizza invece a livello di sistema operativo: usa i **namespace** del kernel Linux (PID, network, mount, user...) per dare a ciascun processo una vista isolata del sistema, e i **cgroup** per limitare e contabilizzare le risorse (CPU, memoria, I/O) che può consumare. Il container condivide il kernel host, quindi è più leggero (avvio in secondi, immagini di pochi MB) ma l'isolamento è più debole di una VM (una vulnerabilità nel kernel espone tutti i container). Per una piattaforma con carichi variabili e necessità di rilasci frequenti, i container sono la scelta corretta; dove un tenant richieda un isolamento più forte, si può adottare un livello aggiuntivo di virtualizzazione leggera (microVM, es. Firecracker, o sandboxed containers come gVisor/Kata) come compromesso.

Kubernetes è l'orchestratore naturale: gestisce il ciclo di vita dei container (scheduling, restart automatico, rolling update), lo **scaling orizzontale**, e offre primitive di isolamento multi-tenant tramite i **Namespace** Kubernetes combinati con **RBAC** (chi può fare cosa su quali risorse), **Resource Quota** (limiti per namespace/tenant) e **Network Policy** (chi può parlare con chi). Per isolamento più stringente si passa a **cluster o node pool dedicati per tenant**, al costo di minore efficienza di utilizzo delle risorse.

**(b) Reti software-defined e segmentazione.** Una rete tradizionale affida la sicurezza soprattutto al perimetro: firewall e VLAN separano l'esterno dall'interno, ma il traffico "east-west" tra servizi interni resta spesso poco controllato — un servizio compromesso può muoversi lateralmente con pochi ostacoli. Una rete **software-defined (SDN)** separa il piano di controllo (decisioni di instradamento, centralizzate e programmabili) dal piano dati, permettendo di applicare policy in modo dichiarativo e dinamico, coerente con la natura effimera dei container.

Un **service mesh** (es. Istio/Linkerd) estende questo controllo al livello applicativo: inietta un **proxy sidecar** accanto a ogni servizio, applicando **mutua autenticazione TLS (mTLS)** tra servizi, autorizzazione fine-grained e — punto centrale per la vigilanza — **osservabilità completa del traffico interno**, utile sia per il debug sia per l'audit trail. Il modello complessivo è **Zero Trust**: nessun servizio è fidato per posizione di rete, ogni comunicazione va autenticata e autorizzata esplicitamente.

**(c) Ingegneria del software sicuro.** Per i componenti critici (validazione e persistenza delle segnalazioni) è preferibile un linguaggio a **tipizzazione forte e statica**, con gestione della memoria sicura by design (garbage collection o ownership/borrow checking), per eliminare intere classi di vulnerabilità (buffer overflow, use-after-free, type confusion) già in fase di compilazione. Per componenti periferici (reportistica, script) linguaggi più dinamici sono accettabili, dato il minor blast radius.

La pipeline **CI/CD** deve incorporare la sicurezza come gate automatico ("shift left"): **SAST** sul codice ad ogni commit, **SCA** sulle dipendenze per individuare librerie con vulnerabilità note, scansione delle **immagini container** prima del push in registry, e firma delle immagini per garantirne integrità e provenienza fino al deployment. Un gate che blocca la promozione in produzione in presenza di vulnerabilità critiche traduce operativamente il principio che un difetto trovato in produzione costa ordini di grandezza più di uno trovato in pipeline.

**(d) Concorrenza e gestione delle risorse.** I servizi possono adottare modelli di concorrenza diversi secondo il profilo di carico: **multi-thread/multi-processo** per carichi CPU-bound (validazione/trasformazione di grandi volumi), dove il parallelismo reale su più core dà throughput; un modello **event-loop asincrono** per servizi I/O-bound con molte connessioni concorrenti ma poco calcolo (API di ricezione). I rischi tipici del multi-threading — **race condition**, **deadlock**, **starvation** — si mitigano con sincronizzazione a grana fine e, quando possibile, preferendo l'immutabilità e il message-passing alla memoria condivisa, che elimina intere classi di race condition per costruzione.

A livello di orchestrazione, i **cgroup** (esposti in Kubernetes come `requests`/`limits`) impongono limiti hard di CPU e memoria per container: è ciò che rende **prevedibile** un ambiente multi-tenant, impedendo che un tenant "rumoroso" degradi le prestazioni degli altri sullo stesso nodo. Lo scheduler del kernel (CFS) e l'OOM killer applicano questi limiti; l'orchestratore vi aggiunge sopra lo scheduling dei pod sui nodi per bilanciare il cluster.

**Esempio nel contesto.** Una piattaforma di raccolta segnalazioni di vigilanza della Banca d'Italia — multi-tenant, con obblighi di audit trail, soggetta a picchi nelle finestre di invio — è esattamente il tipo di sistema per cui container/Kubernetes, service mesh Zero Trust e pipeline CI/CD con gate di sicurezza non sono una moda tecnologica ma la traduzione pratica dei requisiti di **resilienza operativa e sicurezza ICT del Regolamento DORA**: ridondanza e scalabilità, gestione del rischio di terze parti (SCA), test di resilienza, tracciabilità (mesh + logging).

**Rischi residui.** (1) **Superficie di attacco del piano di controllo**: un cluster Kubernetes compromesso espone l'intera piattaforma multi-tenant — richiede hardening specifico (audit log, RBAC minimale, rotazione credenziali). (2) **Complessità operativa**: mesh e orchestrazione aggiungono livelli da monitorare e patchare, con possibile aumento della superficie di attacco complessiva rispetto al monolite. (3) **Vulnerabilità del kernel condiviso**: l'isolamento container è più debole di quello delle VM — una escape vulnerability resta un rischio sistemico. (4) **Supply chain**: la scansione SCA riduce ma non elimina il rischio di vulnerabilità zero-day nelle dipendenze. (5) **Costo di competenze**: la transizione richiede skill nuove (SRE, sicurezza cloud-native) da costruire nel team, con un periodo di transizione a rischio più elevato.

---
---

# AMBITO 2 — Crittografia, DLT, privacy

## Svolgimento Tema 2.1 — Migrazione post-quantum della crittografia istituzionale

**Impostazione.** La minaccia "harvest now, decrypt later" implica che un avversario possa catturare oggi il traffico cifrato e decifrarlo non appena esisterà un computer quantistico crittograficamente rilevante. Per un'istituzione che custodisce **dati riservati di lunga durata** — comunicazioni di vigilanza, statistiche sensibili, infrastrutture di firma/PKI — la pianificazione della migrazione non può attendere il "Q-Day": deve iniziare ora.

**(a) Perché la crittografia a chiave pubblica attuale è vulnerabile.** L'**algoritmo di Shor** risolve la fattorizzazione di interi e il problema del logaritmo discreto in tempo polinomiale su un computer quantistico, rompendo gli schemi **RSA** e a **curva ellittica** (ECDH, ECDSA) che sono alla base di praticamente ogni handshake TLS, aggiornamento firmato e certificato. La crittografia **simmetrica** viene solo *indebolita*: l'**algoritmo di Grover** offre un'accelerazione quadratica, per cui AES-256 mantiene una sicurezza effettiva di circa 128 bit — ancora robusta. Anche le funzioni hash necessitano di output più lunghi (SHA-384/512). Il livello asimmetrico è quindi il problema urgente.

**(b) Gli standard NIST.** Finalizzati nell'agosto 2024:

- **FIPS 203 — ML-KEM** (basato su reticoli, derivato da CRYSTALS-Kyber): un **meccanismo di incapsulamento di chiave (KEM)** che sostituisce RSA/ECDH per stabilire segreti condivisi. ML-KEM-768 è lo standard di default per l'impresa.
- **FIPS 204 — ML-DSA** (basato su reticoli, derivato da CRYSTALS-Dilithium): l'algoritmo di **firma digitale primario**, in sostituzione di RSA-PSS, ECDSA ed EdDSA. Il NIST ne raccomanda l'adozione per primo.
- **FIPS 205 — SLH-DSA** (basato su hash, derivato da SPHINCS+): uno schema di **firma di riserva conservativo**, la cui sicurezza si fonda unicamente sulle proprietà delle funzioni hash — un fondamento matematico diverso, che sopravvive quindi a un'eventuale rottura delle ipotesi sui reticoli.

Una quarta firma, **FN-DSA** (Falcon), è in corso di standardizzazione come FIPS 206; produce firme compatte ma è difficile da implementare senza incorrere in side-channel leak.

**(c) Roadmap di migrazione.** Un programma disciplinato, non un singolo aggiornamento:

1. **Inventario crittografico (CBOM)** — individuare ogni utilizzo di crittografia a chiave pubblica in applicazioni, protocolli, HSM, certificati e firma del codice.
2. **Prioritizzazione basata sul rischio** — migrare per prime i dati con riservatezza a lungo termine (esposti al rischio HNDL) e le radici di firma più critiche.
3. **Modalità ibrida** — combinare un algoritmo classico (es. X25519) con un algoritmo PQC (ML-KEM) in un unico handshake, in modo che il canale sia sicuro se *anche solo uno* dei due regge; questo preserva inoltre la conformità FIPS 140-3 durante la transizione.
4. **Migrazione della PKI** — emettere certificati X.509 ibridi/PQC; pianificare **catene di certificati più lunghe** e chiavi più grandi; verificare che CA, intermediari e edge CDN accettino le dimensioni maggiori.
5. **Agilità crittografica** — progettare i sistemi in modo che gli algoritmi possano essere sostituiti rapidamente; questo è l'obiettivo duraturo, poiché la modalità ibrida è una transizione, non una destinazione.
6. **Tempistiche** — allinearsi alle indicazioni NIST: dismettere gli algoritmi asimmetrici classici entro circa il **2030**, vietarli entro il **2035**.

**(d) Impatto su protocolli e infrastrutture.** **TLS 1.3** acquisisce lo scambio di chiavi ibrido; **IPsec/IKEv2** e l'accordo di chiave **SSH** devono seguire; gli **HSM** necessitano di firmware dei fornitori che supporti le nuove primitive. Chiavi e firme più grandi aumentano la dimensione dell'handshake e della catena di certificati e, potenzialmente, la frammentazione (MTU) e l'impatto sulle prestazioni — tutti aspetti da testare.

**Esempio nel contesto.** Poiché la Banca d'Italia protegge informazioni la cui riservatezza deve durare decenni e gestisce infrastrutture di firma di rilevanza sistemica, la minaccia HNDL è direttamente rilevante; l'agilità crittografica si integra inoltre naturalmente con le aspettative di resilienza operativa di DORA.

**Rischi residui.** (1) **Side-channel di implementazione**, specialmente nel campionamento gaussiano (FN-DSA) — usare librerie validate. (2) **Ecosistema immaturo** e supporto HSM disomogeneo. (3) **Cicli lunghi di sostituzione hardware** per apparati di rete e dispositivi embedded. (4) **Una futura rottura** dello schema scelto — mitigata proprio dall'agilità crittografica unita al backup basato su hash SLH-DSA.

---

## Svolgimento Tema 2.2 — DLT e Privacy-Enhancing Technologies per la finanza tokenizzata

**Impostazione.** Una piattaforma DLT per il regolamento di asset finanziari tokenizzati tra intermediari deve conciliare quattro esigenze in tensione: **finalità e definitività del regolamento**, **riservatezza** delle transazioni, **scalabilità** e **conformità normativa** (GDPR in primis). Le scelte tecnologiche vanno guidate dal fatto che si opera in un contesto **regolamentato e a soggetti noti**, non in una rete pubblica anonima.

**(a) Architettura DLT e consenso.** Una rete **permissionless** (validatori anonimi, PoW/PoS) è inadatta: finalità solo probabilistica, possibilità di *fork*, throughput e costi energetici problematici, e impossibilità di soddisfare KYC/AML. Propongo una rete **permissioned** con un algoritmo di **consenso BFT** (es. PBFT/IBFT): validatori identificati e autorizzati, **finalità immediata e deterministica** (nessun fork, requisito essenziale per la definitività giuridica del regolamento), throughput elevato e bassa impronta energetica. Il PoW si scarta per costo e finalità probabilistica; il PoS riduce i consumi ma resta orientato a reti aperte.

**(b) Smart contract: modello di esecuzione e rischi.** Gli smart contract automatizzano la logica di regolamento (es. *delivery-versus-payment* atomico tra token di asset e token di contante). Il modello di esecuzione deve essere **deterministico** (stesso input → stesso stato su tutti i nodi). Linguaggi: Solidity su macchina EVM, oppure linguaggi pensati per la finanza con maggiori garanzie (es. modelli a risorse come Move, o DAML). **Rischi**: *reentrancy*, overflow, errori logici, manipolazione degli **oracoli** (la fonte dei dati esterni è un *single point of failure*), costi/gas e blocchi. **Contromisure**: audit di sicurezza, **verifica formale**, test estensivi, pattern *checks-effects-interactions*, oracoli ridondanti e affidabili.

**(c) Scalabilità e interoperabilità.** Soluzioni di scalabilità: **layer-2** e **rollup** (optimistic o ZK) che spostano l'esecuzione fuori dalla catena principale mantenendone le garanzie; **sharding** per partizionare il carico; canali per micro-regolamenti. L'**interoperabilità** tra piattaforme eterogenee (diverse DLT, o DLT e sistemi tradizionali) si affronta con *bridge*, schemi *notary*, *hash time-locked contract* (HTLC) per scambi atomici cross-chain e protocolli di messaggistica standardizzati. È un punto critico per evitare la frammentazione in "isole" non comunicanti.

**(d) Privacy e tensione con il GDPR.** Le **Privacy-Enhancing Technologies** consentono riservatezza senza rinunciare alla verificabilità: le **zero-knowledge proof** (zk-SNARK/zk-STARK) provano la validità di una transazione (es. "il saldo è sufficiente") senza rivelarne i dettagli; la **crittografia omomorfica** permette calcoli su dati cifrati; la **secure multiparty computation** consente analisi congiunte senza condividere i dati grezzi. La tensione di fondo è tra **immutabilità della DLT** e **diritto alla cancellazione (GDPR art. 17)**: poiché ciò che è scritto on-chain non si cancella, i **dati personali vanno tenuti off-chain**, registrando on-chain solo *hash*, *commitment* o puntatori; la cancellazione del dato off-chain (o la distruzione della chiave, *crypto-shredding*) rende il riferimento on-chain inintelligibile. Si applicano inoltre minimizzazione e *privacy by design*.

**Esempio nel contesto.** L'Eurosistema sta sviluppando soluzioni per il regolamento all'ingrosso in moneta di banca centrale (wholesale CBDC) e per la finanza tokenizzata, con la Banca d'Italia attiva sul tema; la scelta di reti permissioned con consenso BFT e PET riflette i requisiti di un regolamento sicuro, riservato e definitivo tra intermediari.

**Rischi residui.** (1) **Oracoli** come punto debole. (2) **Gestione delle chiavi** dei validatori e degli intermediari. (3) **Governance** della rete permissioned (chi ammette/revoca i validatori). (4) **Certezza giuridica** della finalità on-chain rispetto al diritto vigente. (5) **Frammentazione** da interoperabilità immatura e rischio nei *bridge* cross-chain.

---
---

# AMBITO 3 — Intelligenza artificiale, machine learning, data science

## Svolgimento Tema 3.1 — Pipeline ML per fraud detection/AML e governance sotto l'AI Act

**Impostazione.** Un sistema di rilevamento frodi e antiriciclaggio basato su ML è, ai sensi dell'**AI Act**, un sistema **ad alto rischio**: ciò condiziona non solo l'architettura tecnica ma anche gli obblighi di governance. Il problema ha inoltre una caratteristica statistica dominante — le frodi sono **eventi rari** — che orienta scelte di modello e metriche.

**(a) Pipeline ML end-to-end.** *Raccolta dati*: transazioni, dati KYC, relazioni di rete tra soggetti. *Preprocessing*: pulizia, gestione dei valori mancanti, encoding. **Feature engineering** (spesso più decisiva della scelta del modello): variabili di *velocity* (frequenza/importo in finestre temporali), aggregazioni per conto/cliente, *feature* di grafo (centralità, comunità — utili per il riciclaggio strutturato), feature temporali. *Scelta dei modelli*:

- **supervisionato** su frodi note: regressione logistica come *baseline* interpretabile, poi **random forest** e **gradient boosting (XGBoost)** per le prestazioni;
- **non supervisionato** per frodi nuove e non etichettate: **anomaly detection** (isolation forest, autoencoder);
- **semi-supervisionato** per sfruttare i pochi casi etichettati insieme alla grande massa non etichettata.

**(b) Sbilanciamento delle classi e metriche.** Con frodi che sono una frazione minima dei casi, l'**accuratezza è fuorviante** (un modello che predice "mai frode" è accuratissimo e inutile). Si usano **precision, recall, F1** e soprattutto l'**AUC-PR** (curva precision-recall, più informativa dell'AUC-ROC in forte sbilanciamento). Tecniche: **resampling** (oversampling/SMOTE, undersampling), **class weighting**, **tuning della soglia** decisionale. Il vero trade-off è tra **recall** (non perdere frodi, costo del falso negativo molto alto in AML) e **precision** (limitare i falsi positivi, che generano *alert fatigue* per gli analisti e attrito per i clienti): la soglia va calibrata sui costi reali, non su un valore astratto.

**(c) Spiegabilità, bias, robustezza.** La spiegabilità non è un optional ma un **requisito di vigilanza**: tecniche come **SHAP** o LIME consentono di motivare perché una transazione è stata segnalata. Vanno valutati **bias e fairness** (assenza di impatto discriminatorio su gruppi protetti) e la **robustezza** del modello. Tutto ciò richiede *monitoring* continuo in produzione (MLOps): le frodi evolvono e il modello soffre di **concept drift**.

**(d) AI Act e model risk management.** Per i sistemi ad alto rischio l'AI Act impone, tra l'altro: **sistema di gestione del rischio**, **governance e qualità dei dati**, **documentazione tecnica**, **logging/tracciabilità**, **sorveglianza umana** (un analista deve poter intervenire), **accuratezza, robustezza e cybersicurezza**, e **valutazione di conformità**. Sul piano interno serve un **model risk management** strutturato: validazione indipendente, monitoraggio delle prestazioni, ricalibrazione e *retraining* periodici.

**Esempio nel contesto.** L'AI Act classifica esplicitamente come ad alto rischio i sistemi di *scoring* creditizio, AML e *fraud detection* oggi in uso nelle banche. Per la Banca d'Italia, autorità di vigilanza, "capire l'IA" significa saperla **governare** — verificare che le banche vigilate usino questi modelli in modo conforme e controllabile — non solo conoscerne le tecniche.

**Rischi residui.** (1) **Concept drift** e **adattamento adversariale** dei frodatori. (2) **Costo operativo dei falsi positivi**. (3) **Qualità del dato** in ingresso. (4) **Trade-off spiegabilità/prestazioni** (i modelli più potenti sono i meno trasparenti). (5) **Rischio di conformità** se la documentazione e la sorveglianza umana sono carenti.

---

## Svolgimento Tema 3.2 — LLM e RAG all'interno dell'istituzione: architettura e governance

**Impostazione.** L'istituzione vuole utilizzare i Large Language Model per aiutare il personale ad analizzare la documentazione regolamentare e di vigilanza, nel rispetto di due vincoli inderogabili: **nessuna esposizione di dati riservati** e **risposte verificabili e tracciabili**. Questi vincoli, più della pura capacità del modello, determinano l'architettura — motivo per cui la **Retrieval-Augmented Generation (RAG)**, e non il fine-tuning, è la spina dorsale corretta.

**(a) Transformer e le opzioni disponibili.** I Transformer si basano sul **self-attention**, che permette al modello di ponderare la rilevanza di ogni token rispetto a tutti gli altri, più gli **embedding** (rappresentazioni vettoriali dense del significato) e la codifica posizionale. Un **foundation model** è pre-addestrato su dati ampi e poi adattato. Tre percorsi di adattamento: **prompting** (nessuna modifica al modello), **fine-tuning** (riaddestrare i pesi su dati di dominio — costoso, statico, e con il rischio di incorporare dati riservati nel modello), e **RAG** (mantenere il modello fisso ma fornirgli, al momento della query, un contesto recuperato e autorevole).

**(b) Un'architettura RAG sicura.**

1. **Ingestione** — i documenti interni vengono suddivisi in chunk e convertiti in embedding, memorizzati in un **database vettoriale** (es. motori della classe pgvector/FAISS) all'interno del perimetro controllato.
2. **Recupero (retrieval)** — la query dell'utente viene trasformata in embedding, si recuperano i top-k chunk più simili; la **ricerca ibrida** (densa + parola chiave/BM25) e un passaggio di **re-ranking** migliorano la precisione.
3. **Generazione** — i passaggi recuperati arricchiscono il prompt; l'LLM risponde **con citazioni ai passaggi sorgente**, così ogni affermazione è tracciabile.

La RAG è preferibile al fine-tuning in questo contesto perché la conoscenza è **dinamica** (la normativa cambia) e **riservata**: i documenti restano in uno store governato, le risposte sono ancorate e attribuibili, gli aggiornamenti non richiedono riaddestramento, e l'allucinazione si riduce perché il modello ragiona sulle evidenze fornite anziché sulla memoria.

**(c) Rischi specifici dell'IA generativa e mitigazioni.** **Allucinazione** → ancoraggio al retrieval, citazione, e rifiuto di rispondere quando manca l'evidenza. **Fuga di dati (data leakage)** → evitare di inviare dati riservati ad API esterne; preferire un deployment **on-premise o su cloud sovrano**, con filtraggio dei PII e controlli di accesso rigorosi. **Prompt injection** (istruzioni malevole nascoste nel contenuto recuperato o inserito dall'utente) → guardrail su input/output, separazione tra istruzioni e dati, accesso agli strumenti secondo il principio del privilegio minimo. **Vendor lock-in e sovranità** → privilegiare modelli aperti/sovrani per gli usi sensibili e progettare per la portabilità. La **valutazione** deve essere esplicita: *groundedness/faithfulness*, rilevanza della risposta e precisione del retrieval, misurate in continuo.

**(d) AI Act e governance.** I modelli di IA per finalità generali comportano obblighi di trasparenza e documentazione tecnica, con regole più stringenti per i modelli "sistemici" più grandi; il deployment deve garantire la **sorveglianza umana** (l'analista valida, il modello assiste) e la sicurezza dei dati. Governance, tracciabilità e capacità di spiegare gli output non sono opzionali ma condizioni d'uso per un'istituzione pubblica.

**Esempio nel contesto.** Per la Banca d'Italia, il valore di un assistente basato su LLM risiede nell'accesso rapido alla propria base di conoscenza, ma la sua ammissibilità dipende da **verificabilità e riservatezza** — esattamente ciò che un sistema RAG ospitato internamente e ancorato a citazioni garantisce, e che un modello esterno opaco non potrebbe offrire.

**Rischi residui.** (1) **Allucinazione residua** anche con l'ancoraggio. (2) **Lacune nel retrieval** (la risposta vale quanto ciò che viene recuperato). (3) Tecniche di **prompt injection in evoluzione**. (4) **Dipendenza operativa** e deriva di modello/versione. (5) **Eccessivo affidamento (over-reliance)** da parte di utenti che trattano gli output come autorevoli senza verifica.

---
---

> **Nota d'uso.** Questi svolgimenti sono *risposte-modello* di riferimento: all'esame conta riprodurne l'**impianto** (impostazione → sviluppo tecnico con specifiche → esempio nel contesto BdI → rischi residui), non memorizzarne il testo. Allena la scrittura *a mano e a tempo* (≈2h per quesito). Ricorda inoltre che la prova prevede un elaborato in lingua inglese: esercitati a scrivere autonomamente in inglese almeno uno di questi svolgimenti.
