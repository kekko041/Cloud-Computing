# Architettura a Microservizi Orientata agli Eventi (Event-Driven Microservices)

L'architettura a **microservizi orientata agli eventi** rappresenta un'evoluzione del classico modello a microservizi. Invece di far comunicare i servizi in modo diretto e sincrono (ad esempio tramite chiamate API HTTP/REST), i servizi comunicano scambiandosi **eventi** in modo asincrono.

In parole povere: un servizio non "ordina" a un altro servizio cosa fare; si limita a notificare al sistema che *qualcosa è successo*, e chi è interessato a quell'informazione reagisce di conseguenza.

---

## Come Funziona l'Architettura?

In un sistema tradizionale (Request-Response), se l'utente acquista un prodotto, il servizio *Ordini* chiama direttamente il servizio *Spedizioni* e attende una risposta. Se il servizio Spedizioni è lento o offline, l'intero processo si blocca.

Nel modello **Event-Driven**, il paradigma cambia radicalmente:

```
[ Servizio Ordini ] --- (Invia Evento: "OrdineCreato") ---> [ Event Broker ]
                                                                 │
                                       ┌─────────────────────────┴─────────────────────────┐
                                       ▼                                                   ▼
                       [ Servizio Spedizioni ]                             [ Servizio Fatturazione ]
                       (Ascolta "OrdineCreato")                            (Ascolta "OrdineCreato")
```

I componenti principali di questa struttura sono tre:

1. **I Produttori (Producers):** I microservizi che generano l'evento. Ad esempio, il servizio *Ordini* crea un evento chiamato `OrdineCreato`.
2. **L'Event Broker (o Message Broker):** Il cuore pulsante del sistema (es. Apache Kafka, RabbitMQ, AWS SNS/SQS). È l'infrastruttura che riceve gli eventi dai produttori e li rende disponibili agli altri.
3. **I Consumatori (Consumers):** I microservizi che si iscrivono (subscribe) a determinati tipi di eventi. Ad esempio, il servizio *Spedizioni* e il servizio *Fatturazione* "ascoltano" l'evento `OrdineCreato` e si attivano in autonomia.

---

## I Vantaggi Principali

Abbandonare le comode chiamate REST offre tre benefici fondamentali:

* **Disaccoppiamento Totale (Loose Coupling):** Il servizio *Ordini* non sa quanti o quali servizi abbiano bisogno di sapere che un ordine è stato creato. Questo permette di aggiungere nuovi servizi (ad esempio, un servizio di statistiche) senza toccare una riga di codice del servizio originale.
* **Alta Resilienza:** Se il servizio *Fatturazione* va offline per manutenzione, l'event broker accumula i messaggi. Quando il servizio torna online, ricomincia a elaborare i dati da dove aveva lasciato, senza che l'utente finale o il resto del sistema se ne accorgano.
* **Scalabilità e Performance:** Poiché le comunicazioni sono asincrone, il sistema non deve attendere che l'intera catena di azioni sia completata per rispondere all'utente. L'interfaccia utente risulta quindi estremamente reattiva.

---

## Le Sfide (Il "Prezzo" da Pagare)

Introdurre gli eventi porta con sé una buona dose di complessità:

* **Consistenza Eventuale (Eventual Consistency):** Poiché i servizi aggiornano i propri database in momenti diversi, i dati non saranno allineati nello stesso identico millisecondo ovunque. Bisogna accettare che il sistema sia "eventualmente consistente".
* **Debugging e Tracciabilità:** Capire cosa è configurato male o cosa è andato storto quando un flusso attraversa molti servizi diversi tramite eventi può essere complesso senza strumenti di *Distributed Tracing* (come Jaeger o OpenTelemetry).
* **Gestione dei Messaggi Duplicati:** A causa di potenziali fallimenti di rete, un evento potrebbe essere inviato più di una volta. I microservizi devono essere progettati per essere *idempotenti*, ovvero capaci di elaborare lo stesso evento più volte senza causare anomalie (es. non addebitare due volte lo stesso pagamento).

---

## Pattern Correlati Comuni

Quando si lavora con questo approccio, si incontrano spesso questi concetti:

* **Event Sourcing:** Invece di salvare solo lo stato attuale di un oggetto nel database, si salva l'intera cronologia degli eventi che lo hanno portato a quello stato.
* **CQRS (Command Query Responsibility Segregation):** Separare nettamente i modelli di scrittura (comandi) da quelli di lettura (query) per ottimizzare le performance complessive.
