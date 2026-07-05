# Sintesi del corso – Introduzione al Cloud Computing

*Documento di studio basato sul materiale del corso (slide prof. L. Catuogno, Università Parthenope, + paper NIST, Montagnani, e Foundations of Cloud/IoT/Edge/Fog).*

Il corso si regge su quattro pilastri: **(1)** origini e principi, **(2)** casi di studio, **(3)** sicurezza, **(4)** virtualizzazione. I primi tre rispondono alla domanda *"cos'è e come funziona il cloud dal punto di vista del cliente e del provider"*; il quarto spiega *"qual è la tecnologia che lo rende possibile"*.

---

## 1. Origini e principi

### Da dove nasce l'idea
L'intuizione precede la tecnologia di decenni. Già nel **1961 John McCarthy** immaginava il calcolo organizzato come una *utility pubblica*, esattamente come la rete telefonica o quella elettrica. Da qui parte una linea evolutiva in tre tappe:

- **Utility Computing** – si adotta il modello economico del servizio: l'oggetto della transazione è la *prestazione*, non lo strumento. Il cliente "compra computazione" come compra energia elettrica, con tariffazione *pay-per-use* (a consumo o a tempo). Un contratto garantisce le prestazioni.
- **Grid Computing** – evoluzione dell'utility computing; il nome richiama la *power grid* elettrica. Si mettono in condivisione risorse generiche (CPU, storage, DB) ma anche speciali (antenne, sensori, telescopi), nell'ambito di un *consorzio* in cui ciascuno contribuisce e attinge secondo le esigenze, con criteri mutualistici. Esempi storici: **SETI@home** (volunteer computing, software BOINC) e **Globus** (file transfer/sharing sicuro tra istituzioni di ricerca).
- **Cloud Computing** – la svolta commerciale arriva nel **2006 con Amazon**: prima **S3** (storage, marzo) poi **EC2** (compute, agosto). L'idea di Bezos: "noleggiare" agli utenti lo spazio disco e il tempo CPU inutilizzati dall'azienda, trasformando capacità in eccesso in un prodotto.

### La definizione NIST (2011)
Il riferimento canonico: il cloud è *un modello per l'accesso di rete ubiquo, comodo e on-demand a un pool condiviso di risorse di calcolo configurabili (reti, server, storage, applicazioni, servizi) che possono essere rapidamente fornite e rilasciate con minimo sforzo di gestione o interazione col provider.*

Da questa definizione il NIST estrae **cinque caratteristiche essenziali**:
1. **On-demand self-service** – il cliente si serve da solo, senza interazione umana col provider.
2. **Broad network access** – accesso via rete, ubiquo, indipendente dal punto di accesso.
3. **Resource pooling** – risorse condivise e assegnate dinamicamente (multi-tenancy).
4. **Rapid elasticity** – le risorse si espandono e contraggono rapidamente secondo il carico.
5. **Measured service** – l'uso è misurato e quantificato (base del *pay-per-use*).

Le slide del corso riassumono i pilastri tecnico-economici in tre parole chiave: **virtualizzazione** (aggregare risorse sparse in un corpus omogeneo), **flessibilità/elasticità** (distribuire le risorse virtuali secondo la variabilità delle richieste) e **pay-per-use** (misurare e fatturare il consumo).

### Gli attori
La catena va dal basso verso l'alto: **IaaS provider** → **PaaS provider** → **SaaS provider** / **Service provider** → **End User**. Ogni livello costruisce sul precedente; chi sta più in alto consuma servizi di chi sta più in basso.

### I modelli di servizio – il "Modello SPI"
È il cuore del corso. Cambia chi gestisce cosa:

- **IaaS (Infrastructure-as-a-Service)** – il provider offre risorse fondamentali (CPU, storage, reti, OS) sotto forma di **macchine virtuali** + strumenti di gestione. Il cliente sceglie l'OS, usa i suoi tool di sviluppo, ma si assume l'onere di amministrare OS e deployment. *Esempio: Amazon EC2.*
- **PaaS (Platform-as-a-Service)** – il provider offre un ambiente di sviluppo completo (linguaggi, librerie, runtime, storage, connettività) + supporto al management. Il cliente sviluppa, rilascia e configura le sue applicazioni senza preoccuparsi dell'infrastruttura sottostante. *Esempi: Google App Engine, Google Colab, Azure.*
- **SaaS (Software-as-a-Service)** – il provider offre applicazioni pronte all'uso. Il cliente le usa (tipicamente via browser, che esegue il *front-end* e dialoga col *back-end* remoto), può personalizzarne la configurazione ma non gestisce né vede l'infrastruttura. *Esempio: Google Apps / Workspace.*

La regola mnemonica: **più si sale (IaaS→PaaS→SaaS), più responsabilità passa dal cliente al provider** e meno controllo (ma anche meno fatica) ha il cliente.

**Modelli "miscellanea":** *Storage-as-a-Service* (es. Dropbox, Amazon S3, spesso classificati come SaaS) e *Hardware-as-a-Service* (di fatto sinonimo di IaaS, enfasi sull'erogare risorse come una piattaforma HW/VM).

### I modelli di deployment – chi possiede e per chi
- **Public Cloud** – servizi al pubblico, infrastruttura di proprietà del provider che la gestisce su apparecchiature proprie.
- **Private Cloud** – servizi interni a una sola organizzazione, per finalità specifiche; gestito dall'organizzazione stessa o in outsourcing. *Esempio: ownCloud (open-source, sync di file in un dominio privato, con cifratura e versioning).*
- **Hybrid Cloud** – composizione di cloud pubblici e privati che restano entità separate ma interconnesse. Concetto chiave: **cloud bursting** – un'app gira sul cloud privato e, quando serve più capacità (*burst*), "trabocca" sul cloud pubblico.
- **Community Cloud** – più organizzazioni federate con obiettivi/esigenze comuni (es. enti governativi, sanità, ricerca) condividono un'infrastruttura con livelli di sicurezza/privacy tarati sulle esigenze della community.

### Service Level Agreement (SLA)
È l'impegno contrattuale del provider verso il cliente. Definisce i **livelli qualitativi garantiti**, i **criteri di misura** (uptime, throughput, response time), le **procedure** di gestione dei problemi e i **risarcimenti** in caso di inadempienza.

**Caso EC2:** AWS si impegna a garantire per ogni singola istanza almeno il **90% di availability su base oraria** (*Hourly Commitment*); sotto soglia, il cliente matura un diritto a *service credit*. Lo SLA è un documento tecnico che prevale sul contratto generale in caso di discrepanze.

**Aspetti controversi** (importante per l'esame): SLA non negoziabili e diversi per ogni provider (difficile confrontarli); gergo aziendale poco chiaro; l'onere di rilevare le violazioni ricade sul cliente, in tempi stretti; i risarcimenti sono quasi sempre a scalare su pagamenti futuri; spesso l'**unica metrica è l'availability**, non le prestazioni reali. Da qui gli sforzi di standardizzazione: **linee guida UE (2014)** e standard **ISO/IEC 19086**.

---

## 2. Casi di studio

Servono a "vedere" i modelli astratti nella pratica. Ciascuno illustra un punto del modello SPI:

- **Dropbox** → Storage/SaaS: sincronizzazione e condivisione file orientata all'utente finale.
- **Amazon EC2** → IaaS: si richiedono *Amazon Machine Instances* (AMI), VM configurabili (da 2 a 32 CPU virtuali, RAM 8–32 GB, vari OS off-the-shelf), collegabili in VPN; si paga per l'uso. È anche il caso di studio dello SLA.
- **Google Cloud SDK** → gli strumenti (CLI/tooling) per interagire programmaticamente con i servizi cloud.
- **Google Colab** → PaaS: ambiente di esecuzione (notebook) fornito come piattaforma, senza gestione dell'infrastruttura.

---

## 3. Cloud Security – principi generali

### Perché il cloud ribalta la sicurezza
Nel modello classico c'è un perimetro: un "dentro" da proteggere e un "fuori" da cui difendersi. **Nel cloud questo confine sparisce.** Attori con interessi potenzialmente in conflitto convivono nello stesso ecosistema e competono per le stesse risorse: "amici" e "nemici" stanno legittimamente fianco a fianco. L'infrastruttura deve quindi offrire un "terreno di gioco" comune e sicuro, impedendo che singoli (o coalizioni di) utenti usino illegittimamente le risorse o danneggino gli altri, risolvendo i conflitti con politiche il meno invasive possibile.

### Le tre "riserve" (concerns) degli utenti
1. **Perdita di controllo (loss of control)** – i dati e i processi non sono più nelle mani del cliente.
2. **Mancanza di fiducia (lack of trust)** – bisogna fidarsi del provider (e dei suoi subappaltatori).
3. **Multi-tenancy (infrastruttura promiscua)** – si condivide l'infrastruttura fisica/logica con altri, anche potenziali avversari. Da qui rischi specifici come i **side-channel attack** (raccolta di info per osservazione indiretta) e i **denial of service** (saturare risorse condivise per danneggiare i vicini).

### Le sfide (gli obiettivi di sicurezza nel cloud)
Si parte dalla triade classica **CIA** e si aggiungono due voci tipiche del cloud:
- **Confidentiality** – i dati restano inintelligibili agli altri utenti e al provider stesso, anche in caso di compromissione.
- **Integrity** – il cliente deve poter verificare che il cloud esegua davvero i servizi richiesti correttamente e che i dati non siano corrotti o manomessi.
- **Availability** – garantire che i dati "siano ancora lì" (*proof-of-retrievability*) e che il servizio regga sotto carico, attacchi DoS o cessazione attività del provider.
- **Privacy** – il provider osserva il comportamento degli utenti per lungo tempo: anche senza violare la confidenzialità, può *inferire* molte informazioni sensibili (es. data mining).
- **Aspetti legali / responsabilità (compliance)** – difficoltà di *auditing* e *analisi forense* su dati fuori dall'organizzazione; il **Legal Dilemma** e la **fiducia transitiva** (se il provider subappalta, i criteri di fiducia restano compatibili?); chi risponde di SOX, HIPAA, GDPR?
- **Vulnerability (riduzione della superficie d'attacco)** – nuovi vettori: il collegamento cliente↔provider, provider↔subappaltatori, e il personale (es. social engineering).

Sul fronte multi-tenancy le contromisure sono: aumentare l'**isolamento** tra tenant (tecniche di strong isolation, requisiti di QoS, policy) e aumentare la **fiducia** (chiarire dov'è il confine di sicurezza e chi è "insider", usando gli SLA per imporre comportamenti fidati).

---

## 4. Tecnologie di virtualizzazione

È il motore tecnologico che rende possibile tutto il resto (pooling, elasticità, multi-tenancy).

### Cos'è la virtualizzazione
In senso lato, creare un *modello generale* di una risorsa reale per modificarne/estenderne percezione e interazione. In informatica: un insieme di tecnologie che introducono un'**interfaccia astratta e standard** tra l'hardware e il software che lo usa, allo scopo di **migliorare l'utilizzo delle risorse** e **semplificare l'interazione con l'hardware**.

### I tre componenti di un sistema virtualizzato
1. **Host** – la macchina/entità le cui risorse sono gestite (di solito l'hardware).
2. **Hypervisor** (o VMM, Virtual Machine Monitor) – lo *strato di virtualizzazione*: controlla le risorse dell'host e le espone attraverso un'interfaccia virtuale. Può fare *hardware abstraction* (riproduce un'architettura HW, es. PC Intel) oppure *OS-level abstraction* (riproduce una vista limitata dell'OS host).
3. **Guest** – chi usa le risorse virtuali (uno o più processi, oppure un intero *Guest OS*); il carico si chiama *payload* o *workload*.

### I tre requisiti fondamentali (Popek & Goldberg)
- **Sicurezza** – l'hypervisor deve avere il controllo completo delle risorse.
- **Equivalenza (fedeltà)** – un programma nella VM si comporta come su una macchina reale.
- **Efficienza** – la maggior parte del codice gira direttamente sull'host; l'hypervisor interviene il meno possibile.

### Tassonomia (dal punto di vista del payload)
- **System level** – il payload è un OS completo; la VM riproduce un intero calcolatore.
- **Process level** – il payload sono uno o più processi; la VM fornisce un *execution environment* che riproduce l'interfaccia dell'OS.

### I due tipi di hypervisor (hardware virtualization)
- **Type-1 (Bare Metal)** – l'hypervisor parte al boot e ha il pieno controllo dell'hardware; eventuale interfaccia minimale solo per management/diagnostica. *Esempi: VMware ESXi, Linux KVM, Nutanix AHV, Proxmox.*
- **Type-2 (Hosted)** – l'hypervisor è un processo dentro un Host OS; mappa le risorse dell'host (es. bridging delle interfacce di rete via device driver), riloca il codice non privilegiato facendolo eseguire all'host ed emula in SW le istruzioni privilegiate. *Esempi: VMware Workstation, VirtualBox, QEMU, VMware Fusion.*

**Come funziona la CPU (prologo sulle modalità):** la CPU opera in *user mode* e *kernel mode*; l'hypervisor introduce un livello di privilegio ulteriore, l'*hypervisor mode*. L'hypervisor avvia un OS, gli assegna la CPU in kernel mode all'interno del suo *time slice*, e periodicamente (o a fronte di errori/shutdown) **riprende il controllo** e passa il turno all'OS successivo. Così nessun OS può toccare gli altri né l'hypervisor.

### Virtualizzazione di rete (Network Virtualization)
Un canale fisico viene suddiviso in più **canali virtuali isolati** (es. VLAN), così lo stesso mezzo fisico è condiviso da più coppie di endpoint come se ciascuna avesse un canale esclusivo. Fondamentale nei *virtual datacenter*, dove coalizioni di VM sono connesse da reti virtuali isolate pur viaggiando sulla stessa rete fisica.

- **Internal Network Virtualization** – comunicazione *tra VM* sullo stesso host: le VM hanno **vNIC** (schede di rete virtuali) connesse a **virtual switch**; ogni vSwitch rappresenta un segmento/VLAN isolato. VM "multi-homed" o virtual appliance possono collegare VLAN diverse.
- **External Network Virtualization** – combina apparati e segmenti fisici. Due operazioni:
  - **Partizionamento**: sistemi su una stessa LAN fisica messi su VLAN distinte (separazione del traffico, sicurezza).
  - **Aggregazione**: una VLAN su segmenti fisici non contigui, anche geograficamente distribuiti (l'astrazione nasconde la discontinuità del mezzo fisico).
- **VLAN Tagging (IEEE 802.1Q)** – il frame ethernet è esteso con un *Tag Control Information (TCI)* che include il **VLAN Identifier (VID)**. Gli switch trattano i frame secondo il tag e la configurazione della porta:
  - **Porte tagged** (assegnate a una VLAN): accettano frame non taggati, applicano il tag in uscita, rimuovono il tag in entrata verso la rete.
  - **Porte trunk**: trasportano frame di un insieme di VLAN propagandoli senza rimuovere il tag.
- **Mista** – combinazione di interna ed esterna (vSwitch + switch fisici/VLAN).

---

## Mappa concettuale rapida (per ripassare)

| Tema | Idea chiave da ricordare |
|------|--------------------------|
| Origini | Utility → Grid → Cloud; McCarthy 1961, Amazon 2006 |
| NIST | 5 caratteristiche essenziali, 3 modelli servizio, 4 deployment |
| Modello SPI | IaaS / PaaS / SaaS: salendo, più carico sul provider |
| Deployment | Public / Private / Hybrid (cloud bursting) / Community |
| SLA | Impegno + metriche (uptime) + risarcimenti; criticità: non negoziabile, solo availability |
| Security | Confine "dentro/fuori" sparisce; 3 riserve (controllo, fiducia, multi-tenancy); CIA + privacy + compliance + vulnerability |
| Virtualizzazione | Host + Hypervisor + Guest; requisiti: sicurezza/equivalenza/efficienza; Type-1 vs Type-2 |
| Rete virtuale | VLAN, 802.1Q tagging, internal/external; vNIC + vSwitch |

---

*Filo conduttore di tutto il corso:* il cloud trasforma il calcolo in un **servizio misurabile ed elastico** (origini + principi), reso possibile dalla **virtualizzazione** (di calcolo e di rete), regolato da **contratti** (SLA) e attraversato da un **problema di fiducia e isolamento** in un ambiente condiviso (sicurezza).
