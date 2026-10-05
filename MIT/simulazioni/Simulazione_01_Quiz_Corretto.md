# Simulazione Prova Scritta — Concorso MIT-EPI (Specialista Informatico)
*Simulazione n. 1 — 60 domande a risposta multipla — VERSIONE CON RISPOSTE EVIDENZIATE*

> Questa è la versione annotata di `Simulazione_01_Quiz.md`: la risposta corretta di ogni domanda è in **grassetto** con ✅. Per lo svolgimento a tempo senza spoiler usa l'altro file; questo serve per il ripasso veloce o per la correzione rapida riga per riga. Le motivazioni estese sono in `Simulazione_01_Soluzioni.md`.

---

1. Chi, in Scrum, è responsabile della gestione del Product Backlog e della massimizzazione del valore del prodotto?
   **a) Product Owner** ✅
   b) Scrum Master
   c) Development Team
   d) Stakeholder esterno

2. Gli investimenti anticipati in hardware tipici di un'infrastruttura on-premise sono classificati contabilmente come:
   a) OpEx
   **b) CapEx** ✅
   c) TCO
   d) ROI

3. Quale livello di isolamento delle transazioni SQL consente il fenomeno del "dirty read" (lettura di dati non ancora confermati da un'altra transazione)?
   a) Serializable
   b) Repeatable Read
   **c) Read Uncommitted** ✅
   d) Read Committed

4. La regola di backup "3-2-1" prescrive:
   a) 2 copie, 1 supporto, 1 offsite
   b) 3 copie sullo stesso supporto, nessuna offsite
   c) 1 copia, 2 supporti, 1 offsite
   **d) almeno 3 copie dei dati, su 2 supporti diversi, con 1 copia offsite** ✅

5. Nel contesto della migrazione cloud, il percorso "Repurchase" consiste in:
   **a) sostituzione dell'applicazione esistente con un prodotto SaaS equivalente** ✅
   b) spostamento delle VM così come sono, senza modifiche
   c) dismissione di sistemi non più necessari
   d) mantenimento dell'applicazione on-premise

6. Cosa distingue fondamentalmente l'apprendimento supervisionato da quello non supervisionato?
   a) Il supervisionato è sempre più veloce da addestrare
   **b) Il supervisionato usa dati etichettati (coppie input-output note), il non supervisionato no** ✅
   c) Il non supervisionato richiede sempre un dataset più grande
   d) Sono due nomi per la stessa tecnica

7. Quale dei principi CIA viene violato quando un dato riservato viene letto da un soggetto non autorizzato?
   a) Integrità
   b) Disponibilità
   **c) Confidenzialità** ✅
   d) Non ripudio

8. In un modello dimensionale per data warehouse, cosa contiene tipicamente la "fact table"?
   a) Solo le chiavi primarie delle dimensioni
   b) Gli attributi descrittivi usati per l'analisi
   c) I metadati di sistema del data warehouse
   **d) Le misure quantitative e le chiavi esterne verso le tabelle delle dimensioni** ✅

9. Il diritto alla portabilità dei dati (art. 20 GDPR) si applica solo quando il trattamento si basa su quali basi giuridiche e con quali modalità?
   **a) Consenso o contratto, ed è effettuato con mezzi automatizzati** ✅
   b) Qualsiasi base giuridica, anche con trattamento manuale
   c) Solo obbligo legale
   d) Solo interesse pubblico

10. Quanti livelli di sicurezza crescente prevede SPID per l'autenticazione?
    a) 2
    **b) 3** ✅
    c) 4
    d) 5

11. Il Piano Triennale per l'Informatica è strutturato in quali tre parti?
    a) Normativa, Tecnologie, Sanzioni
    b) Analisi, Design, Collaudo
    **c) Strategia, Tecnologie, Strumenti** ✅
    d) Strategia, Budget, Audit

12. Qual è la differenza nel regime di vigilanza tra Soggetti Essenziali e Soggetti Importanti secondo la NIS2?
    a) Sono vigilati entrambi solo ex post
    b) Sono vigilati entrambi solo ex ante
    c) Gli Essenziali sono vigilati ex post, gli Importanti ex ante
    **d) Gli Essenziali sono soggetti a vigilanza ex ante, gli Importanti prevalentemente ex post** ✅

13. Quale design pattern creazionale garantisce che una classe abbia una sola istanza, fornendo un punto di accesso globale ad essa?
    **a) Singleton** ✅
    b) Factory
    c) Observer
    d) Adapter

14. Un SLA del 99,9% di disponibilità annua corrisponde approssimativamente a quale downtime massimo tollerato in un anno?
    a) Circa 52 minuti
    **b) Circa 8,7 ore** ✅
    c) Circa 87 ore
    d) Circa 3,65 giorni

15. In un database relazionale, a cosa serve principalmente una chiave esterna (Foreign Key)?
    a) Velocizzare l'esecuzione delle query
    b) Comprimere i dati memorizzati
    **c) Garantire l'integrità referenziale collegando una riga a una riga di un'altra tabella** ✅
    d) Definire il tipo di dato di una colonna

16. Qual è il principale svantaggio di una replica sincrona rispetto a una asincrona?
    a) Rischio più elevato di perdita dati in caso di crash
    b) Impossibilità di eseguire backup
    c) Nessun impatto sulle prestazioni di scrittura
    **d) Maggiore latenza di scrittura, poiché la conferma avviene solo dopo l'ack di tutte le repliche** ✅

17. In Kubernetes, a cosa serve principalmente l'oggetto "Service"?
    **a) Fornire un indirizzo di rete stabile per un insieme di Pod, che sono effimeri e cambiano IP** ✅
    b) Eseguire direttamente il codice applicativo
    c) Memorizzare lo stato persistente del cluster (compito di etcd)
    d) Gestire il build delle immagini Docker

18. Il Random Forest riduce la varianza rispetto a un singolo albero decisionale grazie a quale tecnica?
    a) Boosting sequenziale
    **b) Bagging: ensemble di alberi addestrati su sottoinsiemi casuali di dati e feature** ✅
    c) Discesa del gradiente (gradient descent)
    d) Regolarizzazione L1

19. Perché la firma digitale si basa sulla crittografia asimmetrica anziché su quella simmetrica?
    a) Perché è computazionalmente più veloce della simmetrica
    b) Perché non richiede alcuna chiave crittografica
    **c) Perché la chiave privata, nota solo al firmatario, firma l'hash; chiunque può verificare con la chiave pubblica senza condividere un segreto comune** ✅
    d) Perché cifra l'intero documento anziché il suo hash

20. L'operazione OLAP "roll-up" consiste in:
    a) Aumentare il livello di dettaglio dei dati
    b) Filtrare il cubo su più dimensioni contemporaneamente
    c) Scambiare gli assi di visualizzazione del cubo
    **d) Ridurre il livello di dettaglio aggregando i dati (es. da regione a nazione)** ✅

21. I dati relativi allo stato di salute di una persona rientrano nella categoria disciplinata da quale articolo del GDPR, che richiede condizioni di trattamento più stringenti?
    **a) Art. 9 (categorie particolari di dati)** ✅
    b) Art. 6 (basi giuridiche generali)
    c) Art. 17 (diritto alla cancellazione)
    d) Art. 28 (responsabile del trattamento)

22. L'art. 3 del CAD sancisce quale diritto fondamentale di cittadini e imprese?
    a) Il diritto alla cancellazione dei propri dati (diritto all'oblio)
    **b) Il diritto di comunicare con la PA utilizzando le tecnologie dell'informazione, come diritto soggettivo azionabile** ✅
    c) Il diritto alla portabilità dei dati
    d) Il diritto di accesso agli atti amministrativi

23. Tra i dieci principi guida del Piano Triennale, quale indica che i servizi digitali vanno progettati a partire dai bisogni reali del cittadino/impresa?
    a) Cloud first
    b) Once Only
    **c) Servizi progettati sull'utente (user-centered design)** ✅
    d) API-first

24. L'art. 20 della NIS2 introduce in particolare quale novità rispetto al regime precedente?
    a) L'abolizione dell'obbligo di notifica degli incidenti
    b) Sanzioni rivolte esclusivamente ai fornitori terzi, mai all'ente
    c) L'eliminazione dei controlli ex ante per i soggetti essenziali
    **d) La responsabilità personale dei membri dell'organo di gestione per negligenza grave nella supervisione della cybersicurezza** ✅

25. Quale verbo HTTP è idempotente ed è utilizzato per sostituire interamente una risorsa esistente?
    **a) PUT** ✅
    b) POST
    c) PATCH
    d) CONNECT

26. Cosa distingue una Availability Zone (AZ) da una Region in un provider cloud?
    a) Sono termini sinonimi usati indifferentemente
    **b) Una AZ è un data center fisicamente separato con alimentazione/rete indipendenti all'interno di una Region, che ne raggruppa più d'una in un'area geografica** ✅
    c) Una Region è sempre più piccola di una singola AZ
    d) La distinzione è puramente di marketing commerciale, senza impatto tecnico

27. Quale famiglia di database NoSQL è più indicata per gestire dati time-series ad altissimo volume di scrittura, come i log di sensori IoT?
    a) Document store
    b) Key-value
    **c) Column-family** ✅
    d) Graph database

28. Su un sistema Linux basato su systemd, quale comando si utilizza per avviare un servizio?
    a) service run <servizio>
    b) init <servizio>
    c) apt start <servizio>
    **d) systemctl start <servizio>** ✅

29. Qual è la differenza tra autoscaling orizzontale e verticale in Kubernetes?
    **a) L'orizzontale aggiunge/rimuove repliche di Pod in base al carico, il verticale regola le risorse (CPU/memoria) assegnate a un singolo Pod** ✅
    b) L'orizzontale regola la CPU di un Pod, il verticale ne aggiunge repliche
    c) Sono due nomi equivalenti per lo stesso meccanismo
    d) Nessuno dei due può essere automatizzato

30. Quale protocollo IoT, basato su UDP e su un modello request/response simile a REST, è pensato per dispositivi con risorse hardware molto limitate?
    a) MQTT
    **b) CoAP** ✅
    c) AMQP
    d) HTTP/2

31. Il CVSS (Common Vulnerability Scoring System) assegna un punteggio di gravità su quale scala?
    a) 0-100
    b) 1-5
    **c) 0-10** ✅
    d) Una scala qualitativa A-F

32. Nell'association rule mining, la "confidenza" di una regola "se A allora B" misura:
    a) La frequenza con cui la combinazione A-B compare nel dataset (è il "supporto")
    b) Il numero totale di transazioni analizzate
    c) La correlazione lineare tra due variabili numeriche
    **d) L'affidabilità della regola, cioè la probabilità che si verifichi B dato che si è verificato A** ✅

33. La nomina del DPO (Data Protection Officer) è obbligatoria senza eccezioni per quale tipologia di soggetto?
    **a) Le autorità pubbliche, indipendentemente dalla natura dei dati trattati** ✅
    b) Solo le imprese private con oltre 250 dipendenti
    c) Solo i soggetti che trattano dati biometrici
    d) Non è mai obbligatoria per la Pubblica Amministrazione

34. Dal punto di vista del valore legale, una PEC è equiparabile a:
    a) Una semplice email ordinaria
    **b) Una raccomandata con ricevuta di ritorno** ✅
    c) Un fax certificato senza valore probatorio
    d) Una firma digitale qualificata

35. Dal 2023, la competenza sulla qualificazione di sicurezza dei Cloud Service Provider per la PA è stata trasferita da AGID a quale ente?
    a) DTD
    b) Consip
    **c) ACN** ✅
    d) Ministero dell'Economia

36. Presso quale ente è incardinato il CSIRT Italia, punto di contatto nazionale per le notifiche NIS2?
    a) AGID
    b) DTD
    c) Garante Privacy
    **d) ACN** ✅

37. Quale strumento di Infrastructure as Code è agentless, si connette via SSH e utilizza playbook YAML per il configuration management?
    **a) Ansible** ✅
    b) Terraform
    c) Kubernetes
    d) Jenkins

38. Quale dispositivo di sicurezza è specificamente progettato per filtrare il traffico applicativo HTTP/S contro attacchi come SQL injection e XSS?
    a) Un router di livello 3
    **b) Un WAF (Web Application Firewall)** ✅
    c) Uno switch di livello 2
    d) Un concentratore VPN generico

39. Nel paradigma MapReduce di Hadoop, qual è il compito specifico della fase "Reduce"?
    a) Distribuire il calcolo iniziale sui vari nodi del cluster
    b) Gestire la replica dei blocchi su HDFS
    **c) Aggregare i risultati parziali prodotti dalla fase Map** ✅
    d) Ordinare fisicamente i file sul disco

40. Perché è preferibile usare "sudo" anziché accedere direttamente come utente "root"?
    a) sudo è sempre più veloce nell'esecuzione dei comandi
    b) sudo disabilita il logging per motivi di privacy
    c) root e sudo sono identici in termini di tracciabilità
    **d) sudo consente di tracciare (audit) chi ha eseguito un comando privilegiato e quando** ✅

41. Il "configuration drift" che l'adozione dell'IaC mira a prevenire è:
    **a) Il disallineamento tra ambienti causato da modifiche manuali non tracciate** ✅
    b) Un bug latente nel codice applicativo
    c) Un errore di instradamento tra data center
    d) Una tipologia di attacco DDoS

42. Il "fog computing" si colloca architetturalmente:
    a) Sempre e solo nel data center cloud centrale
    **b) A un livello intermedio tra edge e cloud, distribuendo l'elaborazione su nodi di rete intermedi** ✅
    c) Esclusivamente a bordo del singolo sensore, senza alcuna rete
    d) È semplicemente un sinonimo di edge computing, senza differenze

43. Tra le cinque funzioni core del NIST Cybersecurity Framework, quale riguarda le attività di monitoraggio per individuare tempestivamente un incidente?
    a) Identify
    b) Protect
    **c) Detect** ✅
    d) Respond

44. Secondo il criterio SMART, un buon KPI deve essere, tra l'altro:
    a) Definito una sola volta e mai più rivisto nel tempo
    b) Esclusivamente qualitativo, mai espresso in valori numerici
    c) Deciso unilateralmente senza riferimento a un obiettivo strategico
    **d) Misurabile e temporalmente definito, oltre che specifico, raggiungibile e rilevante** ✅

45. L'art. 32 GDPR, in tema di sicurezza del trattamento, richiede esplicitamente la capacità di garantire quali proprietà dei sistemi?
    **a) Riservatezza, integrità, disponibilità e resilienza dei sistemi e servizi di trattamento** ✅
    b) Solo la riservatezza dei dati trattati
    c) Solo la velocità di elaborazione dei dati
    d) Solo la conformità documentale, senza misure tecniche

46. Qual è la differenza tra IPA e INAD?
    a) Sono due nomi per lo stesso identico registro pubblico
    **b) IPA raccoglie i domicili digitali delle PA, INAD quelli di cittadini, professionisti e imprese** ✅
    c) INAD riguarda esclusivamente le grandi imprese quotate
    d) IPA è gestito da un soggetto privato accreditato

47. Il TCO (Total Cost of Ownership), nella programmazione della spesa ICT pubblica, include oltre al prezzo d'acquisto anche:
    a) Esclusivamente i costi energetici di esercizio
    b) Esclusivamente i costi di formazione del personale
    **c) Manutenzione, formazione, rischio di vendor lock-in e consumo energetico (Green IT)** ✅
    d) Nessun altro costo oltre a quello di acquisto iniziale

48. Le sanzioni amministrative pecuniarie NIS2 per i Soggetti Essenziali possono arrivare fino a:
    a) 5 milioni di euro o l'1% del fatturato globale
    b) 20 milioni di euro o il 4% del fatturato globale (soglia tipica GDPR)
    c) Nessun limite massimo predefinito
    **d) 10 milioni di euro o il 2% del fatturato globale annuo** ✅

49. Tra le categorie OWASP Top 10, in quale rientra tipicamente un attacco di SQL Injection?
    **a) Injection** ✅
    b) Broken Access Control
    c) Security Misconfiguration
    d) Cryptographic Failures

50. Il rischio di dipendenza tecnica/contrattuale da un singolo cloud provider, che rende costosa o complessa la migrazione altrove, si chiama:
    a) Shadow IT
    **b) Vendor lock-in** ✅
    c) Data gravity
    d) Cold start

51. Un sistema distribuito che, in presenza di una partizione di rete, preferisce rifiutare di rispondere piuttosto che restituire dati potenzialmente non aggiornati, sta privilegiando quale combinazione del teorema CAP?
    a) AP
    b) CA
    **c) CP** ✅
    d) Nessuna: è impossibile scegliere in un sistema distribuito

52. In PowerShell, i cmdlet seguono tipicamente quale convenzione di naming?
    a) Sostantivo-Verbo
    b) Solo il nome del comando, senza struttura fissa
    c) Una sintassi identica a quella di Bash
    **d) Verbo-Sostantivo (es. Get-Process, Set-ADUser)** ✅

53. Dove vengono tipicamente distribuite le immagini Docker per essere condivise e scaricate su più host?
    **a) Un registry (es. Docker Hub o un registry privato)** ✅
    b) Direttamente su un nodo etcd del cluster
    c) Un hypervisor dedicato
    d) Un API Gateway

54. Secondo l'AI Act, un chatbot istituzionale che deve dichiarare la propria natura artificiale all'utente rientra nella categoria di rischio:
    a) Inaccettabile
    **b) Limitato (obblighi di trasparenza)** ✅
    c) Alto
    d) Minimo

55. La proprietà di sicurezza del "non ripudio" garantisce che:
    a) I dati non possano mai essere letti da terzi
    b) Il servizio sia sempre disponibile, anche sotto attacco
    **c) Un soggetto non possa negare di aver compiuto una determinata azione (es. grazie a log protetti e firme digitali)** ✅
    d) Un server venga autenticato tramite certificato X.509

56. Qual è la differenza tra le operazioni OLAP "slice" e "dice" su un cubo multidimensionale?
    a) Sono sinonimi della stessa operazione
    b) Slice riduce il dettaglio, dice lo aumenta
    c) Dice si applica solo a dati non strutturati
    **d) Slice fissa un valore su una singola dimensione, dice filtra su più dimensioni contemporaneamente** ✅

57. Il diritto di opposizione (art. 21 GDPR) può essere esercitato dall'interessato rispetto a trattamenti basati su:
    **a) Legittimo interesse o esecuzione di un compito di interesse pubblico** ✅
    b) Consenso esplicito dell'interessato
    c) Esecuzione di un contratto
    d) Obbligo legale cui è soggetto il titolare

58. Il regolamento eIDAS garantisce, tra l'altro, che:
    a) Venga imposta un'unica identità digitale europea obbligatoria per tutti i cittadini UE
    **b) Uno schema di identità digitale notificato da uno Stato membro UE debba essere riconosciuto anche dagli altri Stati membri per l'accesso ai servizi pubblici online** ✅
    c) Si applichi esclusivamente ai servizi digitali privati
    d) Sostituisca integralmente SPID a livello nazionale

59. L'obbligo di pubblicazione proattiva su bandi, appalti, bilanci e performance da parte della PA è disciplinato da:
    a) Il CAD (D.Lgs. 82/2005)
    b) Il Regolamento eIDAS
    **c) Il D.Lgs. 33/2013 (Amministrazione Trasparente)** ✅
    d) Il Codice degli Appalti (D.Lgs. 36/2023)

60. Rispetto alla NIS2, cosa rende il TLPT (Threat-Led Penetration Testing) previsto da DORA una misura più stringente in tema di test di resilienza?
    a) Sono identiche su questo punto, nessuna differenza
    b) La NIS2 vieta esplicitamente i penetration test
    c) DORA non prevede alcun test di resilienza
    **d) DORA rende il TLPT un obbligo mandatorio specifico per le funzioni critiche del settore finanziario, mentre la NIS2 richiede test di resilienza senza uno standard così dettagliato e vincolante** ✅

---

*Fine. Motivazioni estese per ogni risposta in `Simulazione_01_Soluzioni.md`.*
