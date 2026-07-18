# Sintesi: "Cybersicurezza Aziendale" — Guide ACN per PMI (Dipendenti, Dirigenti, Professionisti IT)

Sintesi delle tre guide pubblicate da **ACN (Agenzia per la Cybersicurezza Nazionale)** in `ACN/`:
- `ACN/Indicazioni Dipendenti PMI.pdf`
- `ACN/Indicazioni Dirigenti PMI.pdf`
- `ACN/Indicazioni Professionisti IT PMI.pdf`

Le tre guide condividono la stessa introduzione (contesto NIS2, statistiche PMI) e lo stesso formato: **azioni chiave** + **contenuti di dettaglio** + riquadro "cosa si rischia se non si fa". Sono rivolte in modo complementare ai tre livelli di un'organizzazione — si veda anche [Guida Tecnica ai Framework di Governance IA e Resilienza Digitale UE.md](Guida%20Tecnica%20ai%20Framework%20di%20Governance%20IA%20e%20Resilienza%20Digitale%20UE.md) per l'inquadramento NIS2/DORA/AI Act a livello di governance UE.

## Contesto comune

- **4,5 milioni di PMI italiane** (ISTAT 2023), asse portante dell'economia, spesso nella filiera di operatori che gestiscono infrastrutture critiche.
- Il **15,8%** delle imprese 10-250 addetti ha subito nel 2024 un incidente ICT con impatto su disponibilità/dati (Eurostat), contro il 9,9% nel 2019 — trend in crescita.
- Vettore principale: **errore umano** sfruttato da malware, ransomware, phishing.
- **Tre livelli di responsabilità** complementari (non sovrapposti): dirigenza (pianifica budget e cultura), professionisti IT (implementano le misure), dipendenti (adottano comportamenti sicuri).

---

## 1. Guida per i Dipendenti — 9 azioni chiave

| # | Azione | Punti salienti |
|---|---|---|
| 1 | Partecipazione attiva ad awareness/formazione | La cybersicurezza è responsabilità condivisa; segnalare l'assenza di linee guida ai referenti |
| 2 | Attenzione al social engineering, in particolare phishing | Distingue **phishing** (e-mail), **smishing** (SMS), **vishing** (chiamate), **whaling** (dirigenza, es. finte azioni legali); segnali comuni: link/allegati sospetti, tono allarmistico, errori grammaticali, mittenti non identificabili. IA generativa/deepfake aumentano il rischio di spear phishing |
| 3 | Gestione sicura delle credenziali | Password robuste, non riutilizzate, no dati personali; password manager da fonti attendibili; **MFA** (possesso/conoscenza/inerenza) ovunque possibile |
| 4 | Backup regolare | Solo su dispositivi/cloud autorizzati dall'organizzazione; approccio misto locale+cloud; rimuovere il supporto dopo l'uso |
| 5 | Attenzione alle condivisioni (volontarie e involontarie) | No file sharing non approvato; cifrare gli allegati riservati; **non caricare documenti riservati su strumenti di IA generativa, traduttori online o PDF editor di terze parti**; cautela sui social (no foto/info dell'ambiente di lavoro) |
| 6 | Aggiornamento di software e antivirus | Aggiornamenti automatici da fonti ufficiali; antivirus sempre attivo e aggiornato |
| 7 | Solo applicazioni attendibili e necessarie | No download autonomo dal web; solo store/cataloghi autorizzati; permessi minimi alle app |
| 8 | Lavoro sicuro ovunque (ufficio, smart working, trasferta) | Dispositivi aziendali cifrati, blocco schermo, VPN su reti pubbliche, no stazioni di ricarica USB pubbliche, log-out sistematico |
| 9 | Segnalazione tempestiva di anomalie | Cambiare subito la password se si sospetta una compromissione; spegnere/disconnettere il dispositivo in caso di malware; segnali di compromissione: rallentamenti, blocchi, popup imprevisti |

---

## 2. Guida per i Dirigenti — 6 azioni chiave

| # | Azione | Punti salienti |
|---|---|---|
| 1 | Stabilire obiettivi e diffondere la cultura della cybersicurezza | Obiettivi di sicurezza allineati alla strategia, rivisti almeno annualmente e nei momenti chiave (avvio attività, nuove tecnologie, dopo un incidente) |
| 2 | Conoscere il quadro normativo di riferimento | **NIS2** (D.Lgs. 138/2024, recepisce Direttiva UE 2022/2555): soglie dimensionali (medie/grandi imprese nei settori Allegati I-II), obblighi di notifica; **PSNC** (D.Lgs. 105/2019 conv. L. 133/2019): analisi del rischio annuale sui "beni ICT" strategici, notifica al CSIRT, comunicazione al CVCN per acquisti critici (DPCM 15/6/2021); **GDPR** (Reg. UE 2016/679): controlli di sicurezza sui dati personali, valutazione obbligo DPO (art. 37); **eIDAS** (Reg. UE 910/2014) per i fornitori di servizi fiduciari |
| 3 | Consapevolezza sugli asset critici (interni ed esterni) | Non tutto va protetto allo stesso livello; analisi del rischio estesa anche agli asset gestiti dai fornitori |
| 4 | Nominare e supportare un responsabile per la cybersicurezza | Figura interna o esterna, con budget/risorse dedicate; allineamenti periodici (almeno trimestrali) |
| 5 | Formazione e awareness, estesa alla supply chain | Valutazione delle competenze acquisite, non solo erogazione dei corsi; fornitori e clienti devono raggiungere un livello di consapevolezza analogo |
| 6 | Verificare affidabilità di fornitori e solidità contrattuale | Certificazioni (es. **ISO/IEC 27001**), clausole su sicurezza/conformità/incident notification, richiesta di vulnerability assessment/penetration test periodici sui fornitori |

---

## 3. Guida per i Professionisti IT — 14 azioni chiave

| # | Azione | Punti salienti |
|---|---|---|
| 1 | Identificare 3-5 iniziative cyber prioritarie l'anno | Piano annuale, con supporto della dirigenza |
| 2 | MFA ovunque possibile | Priorità a office automation, cloud storage, credenziali privilegiate, accesso remoto; opzioni: SMS/OTP/push/e-mail/biometria/chiavi fisiche |
| 3 | Procurement sicuro | Requisiti di sicurezza nei contratti, **principio del privilegio minimo** per i fornitori, VA/PT periodici; se la PMI è essa stessa fornitore di un soggetto NIS2, deve garantire risk assessment, continuità, integrità del software, audit |
| 4 | Cloud SaaS come leva di riduzione del carico di sicurezza | Distingue **IaaS / PaaS / SaaS**; con SaaS gran parte della responsabilità di patching/hardening passa al provider — ma va sempre verificata la localizzazione UE dei dati personali (GDPR) |
| 5 | Aggiornamenti e patch, niente OS non supportati | Inventario asset per criticità; criteri di priorità: bug noti, superficie esposta, criticità della vulnerabilità; preferire piattaforme centralizzate di patch management |
| 6 | Cifratura dei dati su tutti gli asset | A riposo (disco, dispositivi removibili) e in transito (HTTPS/TLS); riduce l'impatto di furto/smarrimento dispositivi |
| 7 | Backup regolari e **testati** | Conservati separati dall'ambiente di produzione, cifrati, con test periodici di ripristino completo — cruciale contro ransomware |
| 8 | Nessun diritto amministrativo per gli utenti generici | **Privilegio minimo**, "need to know", **separation of duties**, modello **RBAC**; account amministratore de-privilegiati per l'uso quotidiano; procedura eccezionale "Break the Glass" tracciata |
| 9 | Endpoint protection aggiornata (antivirus, UTM, NGFW) | Preferire soluzioni centralizzate; includere filtro anti-spam/phishing |
| 10 | Accesso remoto sicuro (VPN, modelli Zero Trust) | Verifica dei requisiti minimi di sicurezza del dispositivo prima della connessione; Secure Internet Gateway per servizi cloud; formalizzazione contrattuale degli accessi dei fornitori |
| 11 | Analisi del rischio e monitoraggio delle minacce | Inventario asset critici → risk assessment → monitoraggio continuo, eventualmente con **SIEM**; segnalare bandi regionali "Digitalizzazione e Cybersicurezza" |
| 12 | Ridurre la superficie esposta a Internet | Solo piattaforme essenziali online; **firewall/WAF**, **DMZ**, MFA, VA/PT periodici, reset delle password amministrative di default |
| 13 | Punto di contatto per la gestione degli incidenti | **Modello a 5 fasi**: (1) Pianificazione → (2) Identificazione dell'evento → (3) Gestione (rilevamento/contenimento/eliminazione-recovery) → (4) Notifica (Garante Privacy per data breach; CSIRT Italia su base volontaria) → (5) Miglioramento continuo |
| 14 | Analisi dei rischi cyber di settore | **CSIRT Italia** (presso ACN) come fonte primaria di bollettini di sicurezza; condivisione delle esperienze per ridurre la vulnerabilità collettiva |

---

## Normative citate nelle guide (riferimento rapido)

| Normativa | Riferimento | Oggetto |
|---|---|---|
| **NIS2** | D.Lgs. 138/2024 (recepisce Direttiva UE 2022/2555) | Sicurezza informatica per entità essenziali/importanti; sostituisce la Direttiva NIS (D.Lgs. 65/2018, Direttiva UE 2016/1148) |
| **PSNC** | D.Lgs. 105/2019, conv. L. 133/2019 | Perimetro di Sicurezza Nazionale Cibernetica: beni ICT strategici, notifica al CSIRT, CVCN |
| **GDPR** | Reg. UE 2016/679 | Protezione dati personali; notifica data breach al Garante |
| **eIDAS** | Reg. UE 910/2014 | Identità digitale e servizi fiduciari (firma digitale, PEC) |

> **Nota per l'esame**: il framework NIS2/PSNC/GDPR qui descritto lato "PMI generica" si intreccia con DORA (settore finanziario) e AI Act — vedi la comparazione in [Guida Tecnica ai Framework di Governance IA e Resilienza Digitale UE.md](Guida%20Tecnica%20ai%20Framework%20di%20Governance%20IA%20e%20Resilienza%20Digitale%20UE.md) §5, utile per Banca d'Italia dove il perimetro applicabile è quello finanziario (DORA) più che NIS2/PSNC in senso stretto.

## Collegamenti trasversali per la preparazione al concorso

- **Zero Trust / MFA / privilegio minimo / RBAC** → si integrano con OAuth 2.0 e mTLS del ModI AGID (v. `AGID_Simulazione_Ramo_A.md`).
- **ISO/IEC 27001** come criterio di qualificazione fornitori → collegabile alla qualificazione CSP/SaaS AGID/ACN (v. `Sintesi_Architetture_Qualita_Migrazione.md` §2).
- **Modello di gestione incidenti a 5 fasi** → confrontabile con il ciclo NIST/ISO 27035 e con gli obblighi di notifica DORA (24h) vs NIS2 vs GDPR (72h), già mappati in `Guida Tecnica ai Framework di Governance IA e Resilienza Digitale UE.md`.
- **CSIRT Italia / ACN** → stesso soggetto istituzionale già incontrato come autorità di vigilanza sulla qualificazione cloud della PA (v. `Sintesi_Architetture_Qualita_Migrazione.md` §2) e come autorità di sicurezza nella governance del PSN (v. §3 dello stesso documento).
