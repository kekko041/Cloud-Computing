# Relazione descrittiva di un prodotto Cloud: Snowflake AI Data Cloud

## 1. Classificazione del servizio secondo la definizione NIST

Snowflake si colloca nel modello **SaaS (Software-as-a-Service)**. Lo stesso fornitore lo presenta come *fully managed service*.

La classificazione regge alla verifica sui criteri NIST:

- **L'oggetto della prestazione è la facoltà di utilizzare un software in esercizio sulla piattaforma del provider**: il cliente accede a un data warehouse relazionale già operativo, interrogabile in SQL (ANSI SQL) tramite una web UI (Snowsight), driver JDBC/ODBC o API. Non c'è nulla da scaricare né da installare: Snowflake è cloud-native e non può essere eseguito on-premises.
- **Il cliente non gestisce né controlla l'infrastruttura sottostante** — rete, server, sistemi operativi, storage. Snowflake amministra hardware, tuning, patching, backup e ottimizzazione dei motori di query.
- **Il controllo del cliente è limitato alla configurazione applicativa**: definizione di database e tabelle, dimensionamento dei virtual warehouse, politiche di auto-suspend, ruoli e permessi (RBAC). Esattamente la "limited user-specific application configuration" prevista dal NIST per il SaaS.

*[REINTEGRO 1 — la sfumatura PaaS]*
Va segnalata una zona di confine con il **PaaS**: attraverso Snowpark il cliente può sviluppare ed eseguire proprio codice (Python, Java, Scala) sulla piattaforma, un uso *platform-like* coerente con la definizione NIST di PaaS. Il nucleo del servizio resta però SaaS — l'applicazione è consegnata pronta all'uso e il cliente non controlla l'ambiente di esecuzione sottostante — mentre in letteratura ricorre anche l'etichetta di *DWaaS / DBaaS*, uno di quei "modelli miscellanea" che il NIST non codifica ma che il mercato utilizza.

Il **deployment** primario è il **Public Cloud**: l'infrastruttura è a disposizione del pubblico generale ed è posseduta e gestita dal provider. Snowflake presenta però due particolarità:

- **È un public cloud "di secondo livello"**: Snowflake non possiede data center propri, ma poggia sull'infrastruttura IaaS di AWS, Microsoft Azure e Google Cloud. È dunque un caso di **catena degli attori** (IaaS provider → SaaS provider → end user): Snowflake è simultaneamente cliente di un IaaS e provider di un SaaS. Il cliente finale deve fidarsi non solo di Snowflake, ma anche del cloud provider che quest'ultimo ha subappaltato.
- **Esiste un'edizione a isolamento rafforzato**, la *Virtual Private Snowflake* (VPS), che offre un'istanza dedicata e isolata all'organizzazione. Non è un vero **Private Cloud** secondo il NIST (l'infrastruttura fisica resta del provider e non è dedicata in senso stretto a un solo consumatore), ma ne è la risposta commerciale: si vende un maggior grado di isolamento a clienti con requisiti di compliance stringenti, attenuando la principale riserva del modello pubblico, la **multi-tenancy**.

### Verifica delle cinque caratteristiche essenziali NIST

1. **On-demand self-service**: l'utente crea account, database e virtual warehouse in autonomia, senza interazione umana col provider (trial attivabile online).
2. **Broad network access**: accesso via rete con meccanismi standard — browser, driver JDBC/ODBC, connettori, REST API.
3. **Resource pooling**: architettura multi-tenant sull'infrastruttura condivisa dei cloud provider sottostanti; le risorse di calcolo sono assegnate e riassegnate dinamicamente.
4. **Rapid elasticity**: i virtual warehouse si avviano, sospendono e ridimensionano in pochi secondi; le dimensioni raddoppiano a ogni scatto (da X-Small a 6X-Large) e le edizioni Enterprise supportano il multi-cluster (scaling orizzontale automatico sulla concorrenza).
5. **Measured service**: consumo misurato in *credits*, fatturati al secondo (con minimo di 60 s a ogni avvio del warehouse); lo storage è misurato in TB compressi/mese. Il warehouse sospeso non consuma nulla. Consumo e costo sono monitorabili dal cliente.

---

## 2. Descrizione del servizio e destinatari

Snowflake è una piattaforma cloud per il **data warehousing** e l'analisi dei dati. Consente a un'organizzazione di centralizzare grandi volumi di dati, strutturati e semi-strutturati, e di interrogarli in SQL con prestazioni elevate, senza possedere né amministrare alcuna infrastruttura.

*[REINTEGRO 2 — il filo conduttore dell'architettura]*
L'elemento tecnicamente caratterizzante è la **separazione tra storage e computazione**: il prodotto si articola in tre strati disaccoppiati.

1. **Database Storage** — i dati risiedono in un repository centralizzato su object storage del cloud sottostante (es. Amazon S3), in formato compresso e ottimizzato. Ne esiste **una sola copia**, condivisa da tutti i consumatori.
2. **Query Processing (Virtual Warehouse)** — il livello di calcolo. Un virtual warehouse è un cluster di risorse computazionali (di fatto un gruppo di macchine virtuali) che esegue le query. Ogni warehouse è **indipendente**: non compete per le risorse con gli altri né ne degrada le prestazioni.
3. **Cloud Services** — il "cervello" del sistema: autenticazione, controllo degli accessi, gestione dei metadati, parsing e ottimizzazione delle query, cifratura.

La conseguenza pratica del disaccoppiamento è notevole: reparti diversi possono lavorare **contemporaneamente sulla stessa unica copia dei dati**, ciascuno con il proprio warehouse dimensionato sulle proprie esigenze. Il team finance può usare un warehouse *Large* dalle 8 alle 17, quello marketing un *X-Small* saltuario, e una pipeline notturna un warehouse dedicato — senza che nessuno rallenti gli altri e senza duplicare i dati. Nel modello tradizionale on-premises, con storage e compute fusi in un'unica macchina, tutto questo richiederebbe di dimensionare l'hardware sul picco assoluto e di gestire la contesa delle risorse tra utenti.

Il destinatario tipico è l'**impresa medio-grande e data-intensive**: aziende con carichi analitici significativi, molteplici sorgenti dati e team distribuiti.

*[REINTEGRO 3 — gli utenti, richiesti esplicitamente dalla traccia]*
All'interno dell'organizzazione gli utenti diretti sono i **data engineer** (costruzione di pipeline di ingestione e trasformazione), gli **analyst** e gli utenti di *business intelligence* (che si collegano con Power BI, Tableau, Looker) e i **data scientist** (modelli ML tramite Snowpark).

Non è un prodotto per l'utente finale consumer (differenza sostanziale rispetto a un SaaS come Dropbox), né per il piccolissimo progetto: non esiste un free tier permanente, ma solo una prova gratuita di 30 giorni con crediti inclusi.

### Il modello economico

È un **pay-per-use** rigoroso, articolato su tre "contatori" distinti:

- **Compute**: crediti consumati dai virtual warehouse, fatturati al secondo. Il costo del credito varia per edizione (Standard, Enterprise, Business Critical, VPS), regione e cloud provider.
- **Storage**: canone mensile per TB di dati compressi.
- **Cloud services**: inclusi gratuitamente fino al 10% del consumo di compute giornaliero, poi tariffati.

---

## 3. Vantaggi offerti dal Cloud Computing

### Vantaggi per il Provider

**Economie di scala e multi-tenancy.** Servendo migliaia di clienti sulla stessa infrastruttura condivisa, Snowflake distribuisce i costi fissi (sviluppo, sicurezza, certificazioni, operations) su una base amplissima. Ogni miglioramento del motore di query beneficia simultaneamente tutti i clienti, con costo marginale di distribuzione prossimo a zero — cosa impossibile nel modello a licenza on-premises, dove ogni cliente ha una propria installazione da aggiornare.

**Ricavi ricorrenti e allineati alla crescita del cliente.** Il modello a consumo genera flussi di cassa prevedibili e ricorrenti e, soprattutto, fa crescere il ricavo automaticamente con l'aumentare dei dati e degli utilizzi del cliente (la cosiddetta *net revenue retention*), senza bisogno di rinegoziare licenze.

**Nessun costo infrastrutturale proprio.** Poggiando su AWS/Azure/GCP, Snowflake non possiede data center: applica a se stesso lo stesso vantaggio che offre ai clienti, scaricando il CAPEX sull'IaaS provider sottostante e potendosi espandere in nuove regioni geografiche senza costruire nulla.

**Controllo del ciclo di rilascio e osservabilità.** Con una sola versione del software in esercizio, il provider elimina il costo di supportare release diverse presso clienti diversi, rilascia aggiornamenti in continuo e — grazie al *measured service* — osserva l'uso reale della piattaforma, informazione preziosissima per lo sviluppo del prodotto.

**Distribuzione ed effetti di rete.** Il Marketplace e il data sharing creano un ecosistema: più organizzazioni aderiscono, più diventa conveniente per le altre entrare, alzando i costi di uscita.

### Vantaggi per i clienti

**Eliminazione del CAPEX e del rischio di dimensionamento.** È il vantaggio economico primario dell'*utility computing*: il cliente non acquista server, non affitta uno spazio in un data center, non assume un team di DBA per il tuning. Trasforma un investimento in conto capitale (CAPEX) in un costo operativo variabile (OPEX) proporzionale all'uso effettivo. Soprattutto, si libera dal problema più insidioso dell'on-premises: dover dimensionare l'hardware sul **picco** di carico, pagandolo anche nei lunghi periodi in cui resta inutilizzato.

**Elasticità reale.** Il warehouse sospeso non consuma crediti, e ridimensionarlo o riavviarlo è pressoché istantaneo. Un report trimestrale particolarmente pesante può girare su un warehouse *4X-Large* per venti minuti e poi spegnersi: nel mondo fisico avrebbe richiesto un acquisto hardware permanente. È l'elasticità NIST applicata alla lettera, e si traduce direttamente in denaro risparmiato.

**Time-to-value.** Non essendoci nulla da installare o configurare, la piattaforma è operativa dal momento della sottoscrizione. Il vantaggio non è solo di velocità: elimina un'intera classe di attività (procurement, provisioning, manutenzione, patching, disaster recovery) che non produce valore per il business.

**Accesso a economie di scala e a competenze specialistiche.** Sicurezza (cifratura end-to-end, RBAC, MFA, data masking) e certificazioni di compliance (HIPAA, PCI-DSS) sono fornite *out of the box*: un livello che una singola organizzazione media difficilmente potrebbe raggiungere e mantenere in proprio.

**Condivisione e collaborazione.** Il *data sharing* consente di condividere dati vivi tra organizzazioni diverse, anche su cloud e regioni differenti, senza copie né ETL. È un vantaggio che nasce specificamente dalla natura cloud del prodotto e che sarebbe irriproducibile on-premises.

**Multi-cloud e mitigazione del lock-in.** Snowflake gira indistintamente su AWS, Azure e GCP: il cliente non è vincolato al singolo IaaS provider (resta però il lock-in verso Snowflake).

### Contropartite

- **Perdita di controllo e fiducia transitiva.** I dati — spesso l'asset più sensibile dell'azienda — risiedono su un'infrastruttura di terzi, a sua volta appoggiata su un'infrastruttura di quarti (il cloud provider). La catena della fiducia si allunga, e con essa la superficie di rischio.
- **Imprevedibilità dei costi.** Il rovescio del pay-per-use: una query mal scritta, un warehouse sovradimensionato o dimenticato acceso possono generare costi rilevanti. Il modello premia lo sforzo di gestione: un vantaggio per chi monitora, una trappola per chi non lo fa.
- **Lock-in applicativo.** Superato il lock-in verso il singolo IaaS, resta quello verso Snowflake: migrare altrove un data warehouse maturo, con le sue pipeline e i suoi dashboard, è un'operazione onerosa.
- **Compliance e localizzazione.** Per un'organizzazione europea si pone la questione della collocazione geografica dei dati e della conformità al GDPR — affrontabile scegliendo regioni UE, ma pur sempre una questione da presidiare contrattualmente.

---

## Conclusione

Snowflake è un esempio particolarmente interessante perché incarna simultaneamente i due lati del cloud: è un servizio SaaS erogato ai propri clienti ed è, al tempo stesso, un consumatore di IaaS presso AWS, Azure e Google. La sua architettura a storage e compute disaccoppiati mostra come l'elasticità non sia solo uno slogan commerciale, ma una scelta ingegneristica precisa che si converte direttamente in un modello di pricing e in un vantaggio competitivo. E la sua stessa esistenza — un'azienda che ha costruito un prodotto da miliardi di dollari senza possedere un solo data center — è forse la dimostrazione più eloquente di ciò che il cloud computing ha reso possibile.

---

**URL del prodotto presentato: https://www.snowflake.com**
