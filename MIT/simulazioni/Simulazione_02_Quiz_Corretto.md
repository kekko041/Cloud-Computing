# Simulazione Prova Scritta — Concorso MIT-EPI (Specialista Informatico)
*Simulazione n. 2 — 60 domande a risposta multipla — VERSIONE CON RISPOSTE EVIDENZIATE*

> Questa è la versione annotata di `Simulazione_02_Quiz.md`: la risposta corretta di ogni domanda è in **grassetto** con ✅. Per lo svolgimento a tempo senza spoiler usa l'altro file; questo serve per il ripasso veloce o per la correzione rapida riga per riga. Le motivazioni estese sono in `Simulazione_02_Soluzioni.md`.

---

1. Nel metodo Kanban, a cosa serve principalmente il limite WIP (Work In Progress)?
   **a) Evitare che il lavoro in corso superi la capacità del team, migliorando il flusso** ✅
   b) Stabilire la durata fissa di uno sprint
   c) Definire i ruoli del team (Product Owner, Scrum Master)
   d) Automatizzare il deployment in produzione

2. Quale caratteristica essenziale del cloud computing, secondo la definizione NIST, descrive la fatturazione basata sul consumo effettivo delle risorse?
   a) Rapid elasticity
   **b) Measured service** ✅
   c) Resource pooling
   d) On-demand self-service

3. Cosa richiede la Prima Forma Normale (1NF) di un database relazionale?
   a) Che ogni attributo non-chiave dipenda dall'intera chiave primaria
   b) Che non esistano dipendenze transitive tra attributi non-chiave
   **c) Che ogni cella contenga un valore atomico e che ogni riga sia identificabile univocamente** ✅
   d) Che la tabella non contenga mai più di tre colonne

4. Per ripristinare i dati da un backup incrementale, è necessario disporre di:
   a) Solo l'ultimo backup incrementale
   b) Solo l'ultimo backup full, senza altro
   c) L'ultimo full più l'ultimo differenziale
   **d) L'ultimo backup full più l'intera catena di backup incrementali successivi, applicati in ordine** ✅

5. Il percorso di migrazione cloud denominato "Retain" indica:
   **a) La scelta consapevole di mantenere un sistema on-premise, per vincoli normativi, tecnici o di costo** ✅
   b) La riprogettazione completa dell'applicazione in ottica cloud-native
   c) La sostituzione dell'applicazione con un prodotto SaaS equivalente
   d) Lo spostamento as-is delle VM su infrastruttura IaaS

6. L'algoritmo K-means, a differenza di altre tecniche di clustering, richiede che venga specificato a priori:
   a) Il tasso di apprendimento (learning rate)
   **b) Il numero di cluster k in cui partizionare i dati** ✅
   c) Il numero di layer nascosti della rete
   d) La funzione di attivazione da utilizzare

7. Nella classificazione STRIDE, un attacco di tipo "Spoofing" (furto/falsificazione d'identità) viola principalmente quale proprietà di sicurezza?
   a) Disponibilità
   b) Integrità
   **c) Autenticazione** ✅
   d) Non ripudio

8. Rispetto allo star schema, lo snowflake schema si caratterizza per:
   a) L'assenza di una tabella dei fatti
   b) Tabelle delle dimensioni completamente denormalizzate
   c) L'impossibilità di eseguire query OLAP
   **d) Tabelle delle dimensioni ulteriormente normalizzate in sotto-tabelle, a scapito di query più complesse (più JOIN)** ✅

9. Perché il consenso al trattamento dei dati personali deve essere, tra l'altro, "inequivocabile" (art. 4 e 7 GDPR)?
   **a) Perché deve risultare da un'azione positiva e chiara dell'interessato, senza ambiguità sull'accettazione del trattamento** ✅
   b) Perché deve essere rinnovato ogni 24 ore
   c) Perché deve essere sempre scritto su supporto cartaceo
   d) Perché è sufficiente il silenzio dell'interessato

10. L'art. 9 del CAD sancisce il principio "Open Data by default", secondo cui:
    a) Tutti i dati della PA, senza eccezioni, devono essere resi pubblici
    **b) I dati pubblici, salvo eccezioni di privacy/sicurezza, devono essere pubblicati in formato aperto e leggibile da dispositivi automatici** ✅
    c) Solo i dati statistici nazionali devono essere aperti
    d) L'apertura dei dati è una facoltà, non un obbligo, della PA

11. Tra i dieci principi guida del Piano Triennale, "API-first" significa che:
    a) Le API vengono sviluppate solo a progetto concluso
    b) Si privilegia sempre il modello SaaS rispetto a IaaS
    **c) I servizi digitali devono essere progettati esponendo API fin dall'inizio, come modalità primaria di interazione tra sistemi** ✅
    d) Le API devono essere sempre di tipo SOAP

12. Con quale decreto legislativo l'Italia ha recepito la direttiva NIS2?
    a) D.Lgs. 65/2018
    b) D.Lgs. 82/2005
    c) D.Lgs. 105/2019
    **d) D.Lgs. 138/2024** ✅

13. Il principio "L" dell'acronimo SOLID (Liskov Substitution) afferma che:
    **a) Le sottoclassi devono poter sostituire le classi base senza alterare la correttezza del programma** ✅
    b) Ogni classe deve avere una sola responsabilità
    c) Le interfacce non devono mai essere segregate
    d) Le dipendenze devono sempre puntare verso implementazioni concrete

14. Qual è la differenza tra multi-cloud e hybrid cloud?
    a) Sono termini sinonimi
    **b) Il multi-cloud usa più provider pubblici per evitare vendor lock-in, l'hybrid cloud combina ambienti pubblici e privati/on-premise con orchestrazione tra i due** ✅
    c) Il multi-cloud è sempre meno costoso dell'hybrid cloud
    d) L'hybrid cloud non può mai includere componenti on-premise

15. In un indice composito su più colonne di un database, perché l'ordine delle colonne nell'indice è rilevante?
    a) Non è mai rilevante, l'ottimizzatore riordina sempre automaticamente
    b) Perché determina il tipo di dato delle colonne indicizzate
    **c) Per il principio del "leftmost prefix": l'indice è pienamente efficace solo se la query filtra a partire dalla colonna più a sinistra** ✅
    d) Perché determina esclusivamente lo spazio occupato su disco

16. Il principio RBAC (Role-Based Access Control) consiste nell'assegnare i permessi:
    a) Direttamente a ogni singolo utente, uno per uno
    b) Solo all'amministratore di sistema
    c) In base all'indirizzo IP di provenienza
    **d) A ruoli, a cui gli utenti vengono associati, invece che permesso per permesso** ✅

17. In Kubernetes, un "rolling update" permette di:
    **a) Aggiornare progressivamente le repliche di un'applicazione senza downtime, con possibilità di rollback automatico in caso di errore** ✅
    b) Eliminare immediatamente tutte le repliche precedenti prima di crearne di nuove
    c) Bloccare il cluster durante l'intero aggiornamento
    d) Sostituire manualmente ogni Pod uno alla volta senza automazione

18. La tecnica PCA (Principal Component Analysis) è utilizzata principalmente per:
    a) Classificare dati etichettati in categorie discrete
    **b) Ridurre la dimensionalità di un dataset, mantenendo la maggior parte della varianza informativa** ✅
    c) Addestrare un agente tramite reward e penalty
    d) Generare automaticamente nuove feature etichettate

19. I record DNS DMARC, SPF e DKIM sono usati principalmente come contromisura contro quale tipo di attacco?
    a) SQL Injection
    b) Buffer overflow
    **c) Phishing (spoofing del mittente email)** ✅
    d) Man-in-the-Middle su TLS

20. L'operazione OLAP "pivot" su un cubo multidimensionale consiste in:
    a) Aumentare il livello di dettaglio dei dati
    b) Ridurre il livello di dettaglio aggregando i dati
    c) Selezionare un sotto-cubo filtrando su più dimensioni
    **d) Scambiare gli assi di visualizzazione del cubo per osservare i dati da un'altra prospettiva** ✅

21. Il diritto alla limitazione di trattamento (art. 18 GDPR) si differenzia dal diritto alla cancellazione perché:
    **a) Sospende temporaneamente il trattamento senza cancellare i dati, ad esempio in caso di contestazione della loro esattezza** ✅
    b) Comporta sempre la cancellazione definitiva dei dati
    c) Si applica solo ai dati particolari ex art. 9
    d) Può essere esercitato solo dal Titolare, mai dall'interessato

22. La Firma Elettronica Semplice (FES) si caratterizza per:
    a) L'uso obbligatorio di un certificato qualificato
    **b) L'assenza di requisiti di identificazione forte del firmatario (es. PIN, username/password, firma scansionata), con valore probatorio liberamente valutabile dal giudice** ✅
    c) La piena efficacia probatoria equivalente alla firma autografa
    d) L'uso obbligatorio di un dispositivo sicuro (smart card o HSM)

23. Perché il DTD, a differenza di AGID, non ha un proprio bilancio autonomo?
    a) Perché è stato soppresso nel 2023
    b) Perché AGID ne finanzia direttamente le attività
    **c) Perché è una struttura interna alla PCM, priva di personalità giuridica propria: personale e budget rientrano nel bilancio della PCM** ✅
    d) Perché si finanzia esclusivamente con fondi PNRR

24. Il criterio dimensionale generale per rientrare nel perimetro NIS2 (salvo eccezioni per soggetti critici) riguarda tipicamente:
    a) Solo le microimprese con meno di 10 dipendenti
    b) Esclusivamente le società quotate in borsa
    c) Qualsiasi impresa, senza alcuna soglia dimensionale
    **d) Medie e grandi imprese, con soglie indicative di almeno 50 dipendenti o 10 milioni di euro di fatturato** ✅

25. Rispetto a REST, il principale vantaggio di GraphQL è:
    **a) Permettere al client di specificare esattamente i dati richiesti in un'unica query, riducendo over-fetching e under-fetching** ✅
    b) Essere sempre più veloce in termini di latenza di rete
    c) Non richiedere alcuna forma di autenticazione
    d) Funzionare esclusivamente su protocollo UDP

26. In un'architettura "Active-Passive", il nodo di backup:
    a) Serve traffico contemporaneamente al nodo primario
    **b) Resta inattivo in condizioni normali e subentra solo in caso di guasto del nodo primario** ✅
    c) Viene eliminato automaticamente dopo il primo utilizzo
    d) Deve sempre trovarsi nella stessa Availability Zone del nodo primario

27. HDFS (Hadoop Distributed File System) garantisce la tolleranza ai guasti principalmente tramite:
    a) La cifratura di tutti i blocchi di dati
    b) L'uso esclusivo di dischi SSD
    **c) La replica dei blocchi di dati su più nodi del cluster** ✅
    d) Il backup giornaliero su nastro

28. Qual è la differenza tra il segnale SIGKILL (kill -9) e SIGTERM (kill -15) in Linux?
    a) Sono comandi identici con sintassi diversa
    b) SIGTERM termina sempre più velocemente di SIGKILL
    c) SIGKILL permette al processo di salvare lo stato prima di chiudersi
    **d) SIGKILL termina il processo forzatamente e immediatamente, SIGTERM chiede una terminazione controllata che il processo può gestire** ✅

29. A cosa serve principalmente un Namespace in Kubernetes?
    **a) Fornire una partizione logica del cluster per isolare ambienti, team o progetti diversi** ✅
    b) Eseguire il build delle immagini Docker
    c) Gestire la crittografia del traffico tra Pod
    d) Sostituire la necessità di un Service

30. Il "dropout" nelle reti neurali è una tecnica di:
    a) Ottimizzazione del tasso di apprendimento
    **b) Regolarizzazione, usata per ridurre l'overfitting disattivando casualmente alcuni neuroni durante l'addestramento** ✅
    c) Riduzione della dimensionalità dell'input
    d) Clustering non supervisionato

31. L'ASLR (Address Space Layout Randomization) è una contromisura tipica contro quale tipo di attacco?
    a) Phishing
    b) SQL Injection
    **c) Buffer overflow** ✅
    d) DDoS

32. Il processo di Data Mining è tipicamente inquadrato come fase centrale di un processo più ampio noto come:
    a) ETL (Extract, Transform, Load)
    b) SDLC (Software Development Life Cycle)
    c) CAP (Consistency, Availability, Partition tolerance)
    **d) KDD (Knowledge Discovery in Databases)** ✅

33. L'art. 22 GDPR riguarda il diritto dell'interessato a:
    **a) Non essere sottoposto a una decisione basata unicamente su un trattamento automatizzato, inclusa la profilazione, salvo specifiche eccezioni** ✅
    b) Ottenere la cancellazione definitiva dei propri dati
    c) Essere informato preventivamente di ogni trattamento, senza eccezioni
    d) Richiedere la nomina di un DPO in qualsiasi organizzazione

34. La PDND (Piattaforma Digitale Nazionale Dati) agisce tecnicamente come:
    a) Un data lake centrale in cui transitano fisicamente tutti i dati della PA
    **b) Un control-plane/broker di fiducia che abilita lo scambio dati tra PA, senza che i dati transitino fisicamente da essa** ✅
    c) Un sistema di firma digitale per i documenti della PA
    d) Un registro anagrafico sostitutivo dell'ANPR

35. Il Polo Strategico Nazionale (PSN) è stato affidato in concessione, tramite gara, a quale consorzio?
    a) Google Cloud Italia
    b) Un ente pubblico dipendente da AGID
    **c) TIM (capofila)-CDP Equity-Sogei-Leonardo, costituitisi in PSN S.p.A.** ✅
    d) Il Ministero della Difesa direttamente

36. L'obbligo di "Supply Chain Security" previsto dall'art. 21 della NIS2 richiede ai soggetti in perimetro di:
    a) Vietare qualsiasi fornitore esterno
    b) Occuparsi solo della sicurezza dei propri sistemi interni, ignorando i fornitori
    c) Notificare ogni fornitore al CSIRT Italia prima della firma del contratto
    **d) Includere requisiti di sicurezza rigorosi nei contratti con i fornitori ICT, valutando il rischio anche dei sub-fornitori critici** ✅

37. gRPC, usato per comunicazione interna tra microservizi a bassa latenza, si basa su:
    **a) HTTP/2 e Protocol Buffers, un formato di serializzazione binario** ✅
    b) HTTP/1.1 e payload XML
    c) UDP e formato JSON
    d) SOAP e WSDL

38. Una connessione dedicata come AWS Direct Connect o Azure ExpressRoute serve a:
    a) Sostituire completamente la necessità di un firewall
    **b) Collegare in modo sicuro e con prestazioni garantite un data center on-premise a un ambiente cloud, senza passare da Internet pubblico** ✅
    c) Fornire solo connettività wireless ai dispositivi mobili
    d) Gestire esclusivamente il bilanciamento del carico interno

39. Apache Spark è generalmente più veloce di MapReduce puro su carichi iterativi perché:
    a) Utilizza esclusivamente hardware dedicato
    b) Non richiede mai di leggere dati da disco
    **c) Esegue l'elaborazione in-memory, evitando di scrivere su disco tra uno stage intermedio e l'altro** ✅
    d) Non supporta operazioni di join

40. In Active Directory, qual è la relazione gerarchica tra dominio, albero (tree) e foresta (forest)?
    a) Sono tre termini equivalenti per lo stesso oggetto
    b) Una foresta è un singolo dominio isolato
    c) Un albero contiene più foreste
    **d) Un albero è un insieme di domini correlati, una foresta è l'insieme di uno o più alberi — la struttura gerarchica più ampia** ✅

41. Perché un'architettura event-driven aumenta la resilienza rispetto a chiamate sincrone dirette tra servizi?
    **a) Perché un consumer non disponibile non blocca il producer, grazie al disaccoppiamento tramite eventi/code** ✅
    b) Perché elimina completamente la necessità di gestire gli errori
    c) Perché garantisce sempre la coerenza forte tra i servizi
    d) Perché riduce a zero la latenza di comunicazione

42. Quale architettura di deep learning è più adatta all'elaborazione di dati sequenziali/temporali, come serie storiche di sensori IoT?
    a) CNN (Convolutional Neural Network)
    **b) RNN/LSTM** ✅
    c) Random Forest
    d) K-means

43. In una PKI (Public Key Infrastructure), qual è il ruolo della Certification Authority (CA)?
    a) Cifrare direttamente tutto il traffico di rete
    b) Generare le chiavi private per conto degli utenti e conservarle
    **c) Verificare l'identità del richiedente ed emettere/firmare il certificato digitale che lega una chiave pubblica a un'identità** ✅
    d) Gestire esclusivamente la revoca dei backup

44. La dimensione di qualità del dato che misura l'assenza di contraddizioni tra sistemi diversi che trattano lo stesso dato si chiama:
    a) Accuratezza
    b) Completezza
    c) Tempestività
    **d) Coerenza (consistency)** ✅

45. La comunicazione diretta agli interessati di una violazione di dati personali (art. 34 GDPR) è dovuta quando:
    **a) La violazione presenta un rischio elevato per i diritti e le libertà delle persone, salvo misure come la cifratura che rendano i dati incomprensibili** ✅
    b) Qualsiasi violazione si verifichi, senza eccezioni
    c) Solo se richiesta esplicitamente dal Garante
    d) Solo per violazioni che coinvolgono più di 10.000 interessati

46. La direttiva 2014/55/UE sulla fatturazione elettronica nella PA viene veicolata tecnicamente tramite quale rete, di cui AGID è Authority nazionale?
    a) SPID
    **b) PEPPOL** ✅
    c) PDND
    d) INAD

47. I pareri di congruità tecnico-economica (art. 14-bis CAD) sono vincolanti per la PA in quale caso?
    a) Sempre, per qualsiasi importo di spesa ICT
    b) Mai, sono solo consultivi
    **c) Per gli acquisti tramite Consip/soggetti aggregatori su beni/servizi qualificati come strategici** ✅
    d) Solo per contratti sotto i 10.000 euro

48. Nell'ambito del PSNC (Perimetro di Sicurezza Nazionale Cibernetica), a cosa serve il CVCN (Centro di Valutazione e Certificazione Nazionale)?
    a) Gestire le notifiche di incidente al posto del CSIRT Italia
    b) Sostituire la funzione di vigilanza dell'ACN
    c) Rilasciare le identità digitali SPID
    **d) Valutare e certificare la sicurezza di beni e servizi ICT critici destinati alle infrastrutture del perimetro, prima del loro acquisto** ✅

49. Il DAST (Dynamic Application Security Testing) individua vulnerabilità:
    **a) Testando l'applicazione in esecuzione, simulando attacchi esterni in modalità black-box** ✅
    b) Analizzando il solo codice sorgente, senza eseguire l'applicazione
    c) Analizzando esclusivamente le librerie di terze parti
    d) Solo durante la fase di raccolta dei requisiti

50. Nel modello di responsabilità condivisa, chi è responsabile della sicurezza fisica dei data center in un'architettura IaaS?
    a) Sempre e solo il cliente
    **b) Il provider cloud (sicurezza "del" cloud)** ✅
    c) Nessuno dei due, è un rischio non gestito
    d) Un ente terzo indipendente obbligatorio per legge

51. Quale famiglia di database NoSQL è più indicata per modellare e interrogare relazioni complesse, come una rete di segnalazioni di frode tra soggetti collegati?
    a) Document store
    b) Column-family
    **c) Graph database** ✅
    d) Key-value

52. In IIS (Internet Information Services), a cosa serve un "application pool"?
    a) Memorizzare le password degli utenti del dominio
    b) Gestire la replica dei database
    c) Sostituire la funzione di Active Directory
    **d) Isolare i processi di applicazioni web diverse, in modo che il crash di una non impatti le altre** ✅

53. Le credenziali e le chiavi API in un ambiente cloud non dovrebbero mai essere:
    **a) Hardcoded nel codice o nelle immagini container, ma gestite tramite un vault dedicato con accesso controllato** ✅
    b) Ruotate periodicamente
    c) Associate a un principio di privilegio minimo
    d) Sottoposte ad audit

54. Un sistema di sorveglianza biometrica di massa in tempo reale in spazi pubblici rientra, secondo l'AI Act, nella categoria di rischio:
    a) Minimo
    **b) Inaccettabile (vietato)** ✅
    c) Limitato
    d) Alto, ma consentito con supervisione umana

55. Tra le funzioni core del NIST Cybersecurity Framework, "Recover" riguarda:
    a) L'identificazione preventiva degli asset critici
    b) Il monitoraggio continuo per individuare un incidente
    **c) Il ripristino dei servizi e delle capacità operative dopo un incidente, con lezioni apprese** ✅
    d) L'implementazione delle salvaguardie preventive

56. Nella data governance, chi è tipicamente responsabile operativo della qualità e della corretta gestione di uno specifico dominio di dati?
    a) Il Data Protection Officer
    b) Il Chief Information Officer, in via esclusiva
    c) L'utente finale del dato
    **d) Il data steward** ✅

57. Il Codice Privacy italiano (D.Lgs. 196/2003), dopo la riforma del D.Lgs. 101/2018, resta in vigore in particolare per:
    **a) Le disposizioni relative alle sanzioni penali in materia di trattamento illecito dei dati** ✅
    b) L'intera disciplina generale del trattamento, in sostituzione del GDPR
    c) Le sole disposizioni abrogate dal GDPR
    d) La definizione delle basi giuridiche del trattamento

58. I quattro principi POUR delle WCAG (Web Content Accessibility Guidelines) sono:
    a) Privacy, Ownership, Usability, Reliability
    **b) Percepibilità, Utilizzabilità, Comprensibilità, Robustezza** ✅
    c) Portabilità, Operatività, Universalità, Ridondanza
    d) Protezione, Organizzazione, Uniformità, Resilienza

59. L'iniziativa AGID "Designers Italia" ha lo scopo di:
    a) Certificare la sicurezza dei Cloud Service Provider
    b) Gestire il registro IPA delle pubbliche amministrazioni
    **c) Definire linee guida di design per garantire omogeneità visiva e funzionale dei servizi digitali pubblici** ✅
    d) Rilasciare le identità digitali SPID

60. Dopo la notifica preliminare (24h) e quella di aggiornamento (72h), quale ulteriore adempimento prevede la NIS2 per un incidente significativo?
    a) Nessun altro adempimento è richiesto
    b) Una seconda notifica preliminare dopo 96 ore
    c) La pubblicazione dell'incidente in Gazzetta Ufficiale
    **d) Una relazione finale entro un mese** ✅

---

*Fine. Motivazioni estese per ogni risposta in `Simulazione_02_Soluzioni.md`.*
