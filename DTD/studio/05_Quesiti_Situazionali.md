# Blocco b) — 12 quesiti situazionali DTD1 (≈ 12 punti, **nessuna penalità**)

> Bando, art. 7 c.1 lett. b): *"problematiche tecniche nell'ambito dei progetti o processi di trasformazione digitale… capacità di giudizio… capacità relazionali, comunicative e di utilizzo delle informazioni… coordinamento ed organizzazione del lavoro e gestione dei rapporti con gli stakeholders."*
> Punteggio: **più efficace +1 · neutra +0,375 · meno efficace 0**. ⇒ **Rispondi sempre**: anche la scelta "neutra" vale punti.

## 1. Il modello della risposta "più efficace"
Il funzionario DTD1 ideale è un **tecnico che risolve nel proprio ruolo, con metodo, coinvolgendo le persone giuste**. La risposta migliore di solito:

| ✅ Caratteristiche della risposta più efficace | ❌ Segnali della meno efficace |
|---|---|
| **Agisce subito** sul problema, nel perimetro del proprio ruolo | Rimanda, aspetta che "si risolva da sé", ignora |
| **Analizza i dati/fatti** prima di decidere (log, metriche, evidenze) | Decide d'impulso o sulla base di opinioni |
| **Coinvolge** gli stakeholder rilevanti e **comunica** in modo trasparente | Agisce da solo all'insaputa di tutti / nasconde il problema |
| **Escalation motivata** al responsabile quando la decisione eccede il proprio ruolo, **portando proposte** | Scarica la decisione verso l'alto senza analisi, oppure decide al posto del dirigente |
| Rispetta **norme, sicurezza e privacy** anche sotto pressione | Scavalca le procedure "per fare prima" (es. disattiva i controlli, condivide credenziali) |
| Bilancia **urgenza e qualità**: soluzione tampone + correzione strutturale | Soluzione definitiva rischiosa subito, oppure solo il tampone |
| Orientata al **risultato** e all'**utente finale** (cittadino) | Orientata alla forma, al "non è compito mio", alla colpa |
| Collaborativa nei conflitti: ascolto, criteri oggettivi, mediazione | Scontro, imposizione gerarchica, evitamento |

**La risposta "neutra"** è di solito corretta ma **parziale o tardiva**: delega senza seguire, comunica ma non agisce, applica la regola senza adattarla, risolve solo il sintomo.

### Procedura in 3 passi (≈ 60 secondi)
1. **Elimina** le opzioni con violazioni (sicurezza, norme, privacy), passività o aggressività → di solito sono le "meno efficaci".
2. Tra le restanti, scegli quella che **risolve + coinvolge + documenta**.
3. Se due opzioni sono buone, preferisci quella che **agisce al proprio livello prima di escalare** e che **usa i dati**.

---
## 2. Casi svolti (formato tipico RIPAM, 3 opzioni)

**S1.** Stai coordinando la migrazione al cloud di un servizio di un Comune finanziata dal PNRR. A due settimane dalla scadenza del target, il fornitore segnala che un'integrazione con l'anagrafe richiederà un mese in più.
- A) Comunichi al Comune che il target è perso e attendi le decisioni del dirigente.
- B) Analizzi con il fornitore il piano, individui le attività da parallelizzare o da ridurre di perimetro senza compromettere il target asseverabile, e porti al dirigente un piano di recupero con i rischi residui.
- C) Chiedi al fornitore di saltare i test di integrazione per rispettare la data.
> **B più efficace** (analisi + soluzione + escalation informata); A neutra (trasparente ma passiva); C meno efficace (qualità e sicurezza compromesse).

**S2.** Durante un test scopri che un'API esposta su PDND restituisce più dati personali di quelli necessari all'e-service.
- A) Segnali immediatamente l'anomalia al responsabile e al team, proponi di limitare il payload ai soli dati necessari (minimizzazione) e verifichi con il DPO se configura un data breach.
- B) Correggi da solo il codice in produzione senza informare nessuno, per non creare allarmismi.
- C) Annoti il problema per il prossimo rilascio pianificato tra tre mesi.
> **A** più efficace; C neutra/tardiva; **B meno efficace** (modifica non governata, mancata valutazione del breach). *Nota: B e C sono entrambe deboli; B è peggiore perché viola le procedure.*

**S3.** Due colleghi del tuo gruppo di lavoro sono in disaccordo sull'architettura (microservizi vs monolite modulare) e il conflitto rallenta il progetto.
- A) Organizzi un confronto strutturato con criteri oggettivi (requisiti, costi, competenze, tempi), documenti le alternative e, se non c'è accordo, sottoponi la sintesi al responsabile.
- B) Scegli tu la soluzione che preferisci e la imponi per sbloccare la situazione.
- C) Lasci che risolvano tra loro, evitando di intervenire.
> **A** più efficace; B neutra (sblocca ma senza consenso né criterio); **C** meno efficace.

**S4.** Un'amministrazione locale che supporti ti chiede di adottare subito una soluzione SaaS non qualificata da ACN perché "costa meno e la usano altri".
- A) Accetti, visto che la decisione spetta all'ente.
- B) Spieghi i vincoli normativi (qualificazione dei servizi cloud per la PA), proponi alternative qualificate con caratteristiche equivalenti e aiuti l'ente a fare una comparazione dei costi.
- C) Rifiuti senza spiegazioni e chiudi la richiesta.
> **B** più efficace; A meno efficace (supporto a una scelta non conforme); C neutra/meno efficace — in genere **C** è classificata "neutra" perché rispetta la norma ma è povera dal punto di vista relazionale.

**S5.** Il dirigente ti chiede in giornata un report sull'avanzamento delle migrazioni, ma i dati dei sistemi di monitoraggio sono incoerenti tra loro.
- A) Invii i dati così come sono senza commenti.
- B) Consegni nei tempi il report con i dati consolidati, evidenziando le incoerenze, le fonti usate e le ipotesi adottate, e proponi un'azione per allineare le fonti.
- C) Chiedi una proroga di una settimana per ricostruire tutti i dati.
> **B**; C neutra; A meno efficace.

**S6.** Un fornitore ti offre un invito a una cena di lavoro durante una gara di cui sei componente della commissione tecnica.
- A) Declini, informi il RUP e valuti la necessità di dichiarare un potenziale conflitto d'interessi.
- B) Accetti, perché si tratta solo di una cena.
- C) Declini senza dire nulla a nessuno.
> **A**; C neutra; B meno efficace.

**S7.** In produzione si verifica un incidente: il portale per i cittadini è irraggiungibile il lunedì mattina.
- A) Apri un incidente, attivi il team di supporto e il fornitore secondo le procedure, ripristini il servizio (anche con un workaround), comunichi agli utenti i tempi stimati e, dopo, avvii l'analisi della causa radice.
- B) Cerchi subito la causa radice nel codice prima di qualsiasi altra azione.
- C) Aspetti la segnalazione formale degli utenti per avere evidenze.
> **A** (logica ITIL incident → problem); B neutra; C meno efficace.

**S8.** Ti accorgi che un collega usa le credenziali amministrative di un altro collega assente per completare un'attività urgente.
- A) Lo aiuti a completare l'attività per non bloccare il servizio.
- B) Gli fai notare la violazione, fai interrompere l'uso delle credenziali, attivate la procedura di abilitazione temporanea corretta e segnali l'accaduto al responsabile della sicurezza.
- C) Lo segnali direttamente all'ufficio disciplinare senza parlargli.
> **B**; C neutra (corretta formalmente ma senza risolvere il problema operativo); A meno efficace.

**S9.** Il PM di un altro ufficio ti chiede dati di dettaglio su un progetto, ma non sei sicuro che sia autorizzato a riceverli.
- A) Glieli invii, dato che è un collega dell'amministrazione.
- B) Verifichi con il tuo responsabile o con il titolare del dato i profili di autorizzazione e, nel frattempo, fornisci le informazioni aggregate non sensibili.
- C) Rifiuti e non rispondi più.
> **B**; C neutra/meno efficace; A meno efficace.

**S10.** Il team di sviluppo di un ente propone di rilasciare in produzione il venerdì sera senza la vulnerability scan prevista dalla pipeline, perché lo scanner è in errore.
- A) Autorizzi il rilascio, si farà la scansione lunedì.
- B) Blocchi il rilascio finché lo scanner non viene ripristinato, oppure esegui una scansione alternativa equivalente; informi gli stakeholder del rinvio con la motivazione.
- C) Rimandi la decisione al lunedì senza dare indicazioni.
> **B**; C neutra; A meno efficace.

**S11.** Devi presentare una nuova piattaforma a funzionari comunali con scarsa competenza digitale.
- A) Usi la stessa presentazione tecnica preparata per i fornitori.
- B) Adatti il linguaggio, parti dai benefici per il loro lavoro, mostri un caso pratico, prevedi materiale di supporto e un canale per le domande.
- C) Invii il manuale tecnico via email chiedendo di leggerlo.
> **B**; A neutra; C meno efficace.

**S12.** Ti viene assegnato un nuovo progetto mentre stai già lavorando a due attività con scadenze vicine.
- A) Accetti tutto senza dire nulla e lavori fino a tardi.
- B) Analizzi i carichi, proponi al responsabile una priorità (urgenza/importanza) e possibili soluzioni (ridistribuzione, ripianificazione), poi segui le indicazioni.
- C) Rifiuti il nuovo incarico.
> **B**; A neutra (impegno ma con rischio di qualità); C meno efficace.

**S13.** Un'analisi rileva che il 40% dei Comuni seguiti non ha completato la dichiarazione di accessibilità.
- A) Invii una comunicazione generica di sollecito a tutti.
- B) Segmenti i Comuni per causa del ritardo (mancanza di competenze, di referente, problemi tecnici), predisponi supporto mirato (guide, webinar, help desk) e monitori l'avanzamento con un cruscotto.
- C) Segnali i Comuni inadempienti ad AgID.
> **B**; A neutra; C meno efficace come prima azione.

**S14.** Il fornitore consegna un rilascio software con funzionalità conformi ma documentazione assente e codice non pubblicato nel repository, come invece previsto dal contratto.
- A) Accetti il rilascio, la documentazione arriverà.
- B) Non approvi la verifica di conformità, contesti formalmente la non conformità tramite il DEC/RUP richiamando le clausole contrattuali (riuso, art. 69 CAD) e concordi tempi certi per l'adeguamento.
- C) Scrivi tu la documentazione per non ritardare.
> **B**; C neutra (risultato ottenuto ma costi impropri); A meno efficace.

**S15.** In una riunione con stakeholder di più amministrazioni emergono richieste incompatibili sui requisiti.
- A) Raccogli e documenti le richieste, le classifichi per valore e fattibilità (es. MoSCoW), organizzi un incontro di allineamento e porti le decisioni residue allo steering committee.
- B) Accogli le richieste dell'amministrazione più grande.
- C) Rinvii il progetto finché non si mettono d'accordo.
> **A**; B neutra; C meno efficace.
