# Il Cloud Computing in ottica Banca d'Italia
*(Linee guida architetturali e normative per il concorso)*

Affrontare il tema del **Cloud Computing** nell'ottica della Banca d'Italia (e più in generale del Sistema Europeo di Banche Centrali - SEBC, e della vigilanza bancaria) significa allontanarsi dal concetto di "cloud come semplice hosting" per abbracciare una visione in cui il cloud è un **ecosistema critico da governare**. 

Le istituzioni finanziarie e le Banche Centrali guardano al cloud con grande interesse per i benefici in termini di scalabilità e agilità, ma lo approcciano con estrema cautela a causa dei rischi sistemici. Ecco i pilastri architetturali e normativi per trattare questo tema:

## 1. La Governance dell'Outsourcing e le Linee Guida EBA/DORA
Per la Banca d'Italia, migrare servizi in cloud equivale a un'esternalizzazione (outsourcing) di funzioni aziendali.
* **Funzioni Critiche o Importanti (FCI):** Se un sistema di pagamento o un database di vigilanza viene spostato in cloud, si applicano regole rigidissime (Linee guida EBA sull'outsourcing e Regolamento DORA).
* **Audit e Ispezioni:** Il contratto con il Cloud Service Provider (CSP, come AWS, Azure, Google Cloud) deve garantire alla Banca d'Italia e alle autorità europee il **diritto illimitato di ispezione e audit** sui data center del fornitore.
* **Vendor Lock-in e Exit Strategy:** È inaccettabile che una banca centrale diventi "ostaggio" di un singolo fornitore. Ogni architettura cloud deve prevedere un piano di uscita testato e documentato, garantendo la portabilità dei dati e delle applicazioni verso un altro provider o il ritorno on-premise (re-patriation) in tempi certi e senza interruzioni del servizio (RTO e RPO compatibili con la Business Continuity).

## 2. Architetture Cloud-Native, Agnostiche e Ibride
Per mitigare il rischio di lock-in e garantire la resilienza, l'architettura tecnica privilegiata è quella **Ibrida e Multi-Cloud**.
* **Containerizzazione e Standard OCI:** Le applicazioni non vengono scritte per girare su un cloud specifico, ma pacchettizzate in container (es. Docker) e orchestrate con Kubernetes. Questo garantisce che l'applicativo possa girare indistintamente nel data center della Banca o su qualsiasi provider pubblico.
* **Infrastructure as Code (IaC):** L'infrastruttura deve essere dichiarativa (es. tramite Terraform), permettendo di ricreare interi ambienti in pochi minuti in caso di disastro.

## 3. Sovranità dei Dati e Sicurezza (Data Sovereignty)
La gestione del dato è il cuore pulsante. I dati finanziari, macroeconomici o di vigilanza sono altamente sensibili.
* **Localizzazione dei dati:** I dati devono risiedere fisicamente all'interno dell'Unione Europea o dello Spazio Economico Europeo (SEE) per garantire l'applicazione del GDPR e impedire l'accesso da parte di governi extra-UE (es. problemi legati al CLOUD Act statunitense).
* **Cifratura e Gestione delle Chiavi (BYOK/KYOK):** Nel cloud pubblico, i dati devono essere cifrati "at rest", "in transit" e sempre più "in use" (Confidential Computing). La Banca deve adottare paradigmi come *Bring Your Own Key* (BYOK) o *Keep Your Own Key* (KYOK), dove il provider cloud ha i dati cifrati ma le chiavi crittografiche rimangono fisicamente nei server on-premise della Banca d'Italia (Hardware Security Module - HSM).

## 4. Il Modello di Responsabilità Condivisa (Shared Responsibility Model)
Un candidato esperto ICT deve aver ben chiaro che **andare in cloud non trasferisce il rischio al fornitore**.
* In ambito IaaS (Infrastructure as a Service), la Banca d'Italia rimane responsabile dell'aggiornamento dei sistemi operativi, delle patch, della gestione degli accessi (IAM - Identity and Access Management) e della configurazione dei firewall virtuali.
* L'adozione del paradigma **Zero Trust** è obbligatoria: nessuna entità (nemmeno un dipendente del provider cloud) ha un "trust" predefinito. Ogni accesso alle interfacce di management del cloud deve essere filtrato, loggato e soggetto a MFA (Autenticazione Multi-Fattore) e PAM (Privileged Access Management).

## 5. Resilienza Operativa (Cloud Disaster Recovery)
In caso di fallimento di una "Availability Zone" (AZ) o di un'intera regione cloud, i servizi della Banca non possono fermarsi.
* **Architetture Active-Active:** I servizi critici devono essere distribuiti su più Data Center (sia fisici della Banca che virtuali su Cloud) che operano in simultanea. Se un nodo cade, il traffico viene reindirizzato istantaneamente (Global Server Load Balancing).

---

> [!TIP]
> **Come impostare un tema sul Cloud all'Esame**
> In sede di esame, non limitarti a dire "spostiamo tutto sul cloud per risparmiare costi". Dimostra invece cautela istituzionale. Spiega che il passaggio al cloud è un enabler di innovazione, ma deve avvenire in modo **graduale**, adottando un approccio **Ibrido** (dati core on-premise, front-end e analitiche scalabili sul cloud), garantendo la portabilità tramite **Kubernetes** e tutelando la **sovranità crittografica** delle informazioni.
