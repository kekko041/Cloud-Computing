# Big Data e Data Engineering
*(Focus per il concorso Esperto ICT - Banca d'Italia)*

In un'epoca guidata dai dati, la Banca d'Italia gestisce moli informative gigantesche (transazioni interbancarie, flussi di mercato, dati macroeconomici, log di sicurezza). L'ingegnerizzazione di questi dati (Data Engineering) è essenziale per abilitare l'Intelligenza Artificiale, l'analisi predittiva e la vigilanza prudenziale.

---

## 1. L'Evoluzione delle Architetture Dati

### 1.1 Dal Data Warehouse al Data Lake
*   **Data Warehouse (DWH):** Progettato per dati *strutturati* e analisi di Business Intelligence storiche. I dati subiscono un processo **ETL** (*Extract, Transform, Load*): vengono prima puliti e trasformati e poi caricati. Problema: poco flessibile e costoso per volumi enormi o dati non strutturati.
*   **Data Lake:** Un repository centralizzato che immagazzina dati in formato *grezzo* (strutturati, semi-strutturati come JSON, e non strutturati come PDF o immagini). Usa il processo **ELT** (*Extract, Load, Transform*): i dati vengono salvati così come sono, e la trasformazione avviene solo quando un data scientist ne ha bisogno (Schema-on-read). 

### 1.2 L'Architettura Moderna: Data Lakehouse
Per unire i vantaggi del DWH (affidabilità, transazioni ACID, query SQL veloci) con quelli del Data Lake (scalabilità infinita e basso costo per dati non strutturati), il settore sta adottando il **Data Lakehouse** (tecnologie come Delta Lake o Apache Hudi).
*   Permette di avere affidabilità transazionale e versionamento dei dati direttamente sui file system a oggetti (es. AWS S3 o storage compatibile on-premise).

---

## 2. Elaborazione: Batch vs Streaming

La Banca d'Italia deve analizzare flussi continui (es. rilevamento frodi in tempo reale sui bonifici istantanei).
*   **Batch Processing (Elaborazione a Lotti):** Analisi eseguite su enormi blocchi di dati a intervalli programmati (es. calcolo dei saldi a fine giornata). Strumenti tipici: Apache Hadoop, Apache Spark (in modalità batch).
*   **Stream Processing (Elaborazione in Tempo Reale):** I dati vengono elaborati non appena sono generati, evento per evento (Event-Driven Architecture). 
    *   **Apache Kafka:** È lo standard industriale per il broker di messaggi distribuiti. Funge da "sistema circolatorio" centrale ad altissimo throughput, disaccoppiando i sistemi sorgente dai sistemi di analisi (es. Spark Streaming o Apache Flink).

---

## 3. Data Governance e Data Quality

Per una Banca Centrale, un dato impreciso può causare danni reputazionali e sistemici irreparabili. Le architetture Big Data non hanno valore senza una rigida **Data Governance**.

*   **Data Lineage:** La tracciabilità completa del ciclo di vita del dato. Sapere esattamente da quale sistema sorgente proviene un'informazione, quali trasformazioni ha subito (ETL pipeline) e chi l'ha consumata. Essenziale in fase di ispezione e auditing.
*   **Master Data Management (MDM):** Creazione di un'unica fonte di verità (Single Source of Truth) aziendale per i dati critici (es. anagrafiche degli enti creditizi), evitando i "silos" dipartimentali isolati.
*   **Data Quality (DQ):** Implementazione di regole automatiche nelle pipeline dati (Data Observability) per bloccare in tempo reale record anomali (es. valori nulli o fuori range) prima che inquinino il Data Lakehouse o addestrino erroneamente un modello di Intelligenza Artificiale.
