# ISO 20022 e T2 / TARGET
### Il rapporto tra lo standard e le infrastrutture di regolamento dell'Eurosistema · Concorso Banca d'Italia 2026 (Profilo A)

> Questo è il tassello che, a un colloquio o in un elaborato, mostra che non conosci solo lo *standard* ma anche le *infrastrutture reali* che lo usano — e il ruolo che la Banca d'Italia vi svolge. È uno dei punti più "spendibili" del tuo profilo.

---

## 1. Cosa sono le TARGET Services
**TARGET** (*Trans-European Automated Real-time Gross settlement Express Transfer system*) è l'insieme delle infrastrutture di mercato dell'Eurosistema per la libera circolazione di **contante, titoli e garanzie**. Comprende quattro servizi di regolamento, più componenti comuni:

| Servizio | Funzione | Note |
|---|---|---|
| **T2** | Regolamento **pagamenti all'ingrosso** in moneta di banca centrale | Composto da **RTGS** + **CLM** (vedi §3) |
| **T2S** (TARGET2-Securities) | Regolamento **titoli** (delivery-versus-payment) | In esercizio dal 2015–2017 |
| **TIPS** (TARGET Instant Payment Settlement) | Regolamento **pagamenti istantanei** al dettaglio | 24/7/365 |
| **ECMS** (Eurosystem Collateral Management System) | Gestione armonizzata del **collateral** | Operativo da **giugno 2025** |
| *Componenti comuni* | **ESMIG** (gateway unico di accesso), **CRDM** (dati di riferimento) | Trasversali ai servizi |

Tutti questi servizi sono **nativi ISO 20022**.

---

## 2. Da TARGET2 a T2: la consolidation e il ruolo dello standard
- Il primo RTGS dell'Eurosistema fu **TARGET**; nel 2007–2008 gli succedette **TARGET2**, su piattaforma unica condivisa (SSP).
- Con il progetto **T2-T2S Consolidation** (parte della strategia *Vision 2020*), il **20 marzo 2023** TARGET2 si è evoluto in **T2**, integrando in un'unica piattaforma le funzionalità di RTGS e di gestione centralizzata della liquidità.
- **Il salto tecnologico chiave della migrazione è proprio l'adozione nativa di ISO 20022** (in comune con T2S, TIPS ed ECMS), insieme alla predisposizione multivaluta.

> Punto da far notare: la migrazione a ISO 20022 di T2 (marzo 2023) è **precedente** e **distinta** rispetto alla fine della coesistenza MT su SWIFT/CBPR+ (novembre 2025). Sono due binari: le **infrastrutture di mercato (PMI)** e la **rete di corrispondenza bancaria (SWIFT)** hanno seguito calendari propri. Confonderli è un errore frequente.

**Base giuridica**: Indirizzo (UE) 2022/912 della BCE. Le componenti nazionali di T2 sono i successori legali di quelle di TARGET2; per l'Italia, **TARGET-Banca d'Italia** subentra a TARGET2-Banca d'Italia. Vale la **Settlement Finality Directive 98/26/CE** (definitività e irrevocabilità del regolamento anche in caso di insolvenza del partecipante).

---

## 3. Dentro T2: RTGS + CLM, e i messaggi ISO 20022 che vi circolano
T2 integra due servizi:
- **RTGS** (*Real-Time Gross Settlement*): regola **una-a-una**, in via continuativa, in moneta di banca centrale e con **definitività immediata**, le transazioni interbancarie, i pagamenti per conto della clientela e le operazioni dei sistemi ancillari.
- **CLM** (*Central Liquidity Management*): gestione **accentrata della liquidità** per tutti i servizi TARGET (RTGS, T2S, TIPS) tramite un conto principale (MCA); vi si regolano anche le operazioni di politica monetaria e il credito infragiornaliero.

**Messaggi ISO 20022 tipici in RTGS** (esempi da saper citare):
| Messaggio | Uso |
|---|---|
| `pacs.008` | Bonifico per conto della clientela (customer credit transfer) |
| `pacs.009` | Pagamento tra istituzioni finanziarie |
| `pacs.004` | Storno / return di un pagamento |
| `pacs.010` | Addebito diretto tra banche (su autorizzazione) |
| `pacs.002` | Status report (esito del pagamento) |
| `camt.05x` | Reporting e notifiche di conto |

L'accesso avviene in modalità **A2A** (application-to-application) o **U2A** (user-to-application) attraverso **ESMIG**; i messaggi trasportano un **Business Application Header (BAH)** con l'identità di *Technical Sender* e *Business Sender*.

---

## 4. Il ruolo della Banca d'Italia (il cuore dell'aggancio)
Le TARGET Services sono **sviluppate e gestite, per conto dell'Eurosistema, dalle "4CB"**: **Banca d'Italia, Banco de España, Banque de France, Deutsche Bundesbank**. In dettaglio:

- **T2 e T2S**: la **Banca d'Italia coordina la gestione operativa insieme alla Deutsche Bundesbank** — monitoraggio dei livelli di servizio, manutenzione ed evoluzioni, profili amministrativi, legali e di **sicurezza**, e responsabilità delle **infrastrutture informatiche** su cui gira il sistema.
- **TIPS**: è stato **sviluppato ed è gestito interamente dalla Banca d'Italia** — è il fiore all'occhiello tecnologico dell'Istituto sui pagamenti istantanei.
- **ECMS**: realizzato e gestito dalle 4CB, operativo da giugno 2025.
- A livello nazionale la BdI gestisce anche **BI-Comp** (compensazione dei pagamenti al dettaglio, regolati poi in T2) e la piattaforma **GEPA**.

> Perché conta per te: significa che la Banca d'Italia **non è solo un utente** di queste infrastrutture, ma un **service provider tecnologico** dell'Eurosistema. Un Esperto ICT può trovarsi a lavorare proprio su sistemi di questa criticità — ed è esattamente il contesto in cui ISO 20022, l'alta affidabilità e la sicurezza si incontrano.

---

## 5. Requisiti non funzionali: cosa rende T2 un caso di studio perfetto
Questi numeri e scelte architetturali sono oro per un tema su "sistemi ad alta disponibilità" (es. Tema 1.1 del Profilo A):

- **Continuità operativa**: infrastruttura consolidata T2/T2S distribuita su **quattro siti in due region distinte** (protezione da disastro locale *e* regionale).
- **Livello di servizio contrattuale**: il **95% delle transazioni** deve essere regolato in **meno di 2 minuti** (nel 2024 il dato reale è stato **99,73%**).
- **Regolamento lordo**: elimina l'intervallo tra cicli di compensazione → **riduce il rischio di regolamento**, a fronte di un maggiore fabbisogno di **liquidità infragiornaliera**.
- **Scala sistemica**: nel 2024 circa **108 milioni** di transazioni annue, media giornaliera ~**421.875** pagamenti per ~**1.811 miliardi di euro**; ~**40.000 banche** raggiungibili nel mondo.
- **Multivaluta**: da **aprile 2025** T2 regola anche in **corone danesi** (lavori in corso per la corona svedese).

---

## 6. Come usarlo in un elaborato (paragrafo-modello)
> "Un esempio concreto di sistema di regolamento ad alta criticità è **T2**, l'RTGS dell'Eurosistema operativo dal marzo 2023, sviluppato e gestito dalle quattro banche centrali tra cui la **Banca d'Italia**. T2 adotta nativamente lo standard **ISO 20022** (i pagamenti interbancari viaggiano come `pacs.008`/`pacs.009`) e regola le transazioni **una-a-una con definitività immediata** in moneta di banca centrale — una scelta **CP** nel teorema CAP, dove la consistenza forte prevale sulla disponibilità eventuale. La resilienza è garantita da **quattro siti su due region** e da un livello di servizio contrattuale (95% dei pagamenti regolati in meno di due minuti), coerente con i requisiti del Regolamento **DORA**."

---

## 7. Errori da evitare
- **Non** confondere la migrazione ISO 20022 di **T2** (marzo 2023, infrastruttura di mercato) con la fine della coesistenza **SWIFT/CBPR+** (novembre 2025, rete di corrispondenza): binari diversi.
- **Non** dire che T2 "è TARGET2": T2 è la **terza generazione**, dal marzo 2023, con CLM e ISO 20022 nativi.
- **Ricordare** che **TIPS** è il servizio interamente **made in Banca d'Italia** — è il dettaglio che personalizza e rafforza la risposta.
- **T2S** = titoli (DvP); **T2** = contante all'ingrosso; **TIPS** = istantanei; **ECMS** = collateral. Non scambiarli.
