# Materia 4 — Amministrazione di Database e Sistemi Operativi Unix/Windows Server
*Materiale di studio per la prova scritta del concorso MIT-EPI (60 quesiti a risposta multipla, 70 minuti)*

---

## 1. Backup e strategie di recovery

### 1.1 Tipologie di backup

| Tipo | Cosa salva | Tempo di backup | Tempo di ripristino | Spazio richiesto |
|---|---|---|---|---|
| **Full (completo)** | tutti i dati | alto | basso (un solo file da ripristinare) | alto |
| **Incrementale** | solo i dati modificati dall'**ultimo backup** (full o incrementale) | basso | alto (serve l'ultimo full + tutta la catena di incrementali) | basso |
| **Differenziale** | solo i dati modificati dall'**ultimo full** | medio (cresce nel tempo) | medio (serve solo l'ultimo full + l'ultimo differenziale) | medio |

*Sintesi per l'esame*: se la domanda chiede "quale backup richiede il minor tempo di ripristino dopo un full", la risposta corretta tra incrementale e differenziale è **differenziale**, perché basta applicare un solo file oltre al full (l'incrementale richiede l'intera catena in ordine).

### 1.2 Strategie e metriche
* **Regola 3-2-1:** almeno 3 copie dei dati, su 2 supporti diversi, con 1 copia offsite (fuori sede).
* **RPO (Recovery Point Objective):** quantità massima di dati (in termini di tempo) che l'organizzazione può permettersi di perdere — determina la frequenza dei backup.
* **RTO (Recovery Time Objective):** tempo massimo accettabile per ripristinare il servizio dopo un incidente.
* **Backup immutabili:** copie che non possono essere modificate/cancellate per un periodo definito (WORM — Write Once Read Many), fondamentali contro attacchi ransomware (requisito richiamato anche dalla NIS2).
* **Test di restore periodici:** un backup non testato non è un backup affidabile — va verificata periodicamente la capacità effettiva di ripristino.

## 2. Replica dei database
* **Master-Slave (Primary-Replica):** un nodo master accetta tutte le scritture e le propaga a uno o più slave/replica in sola lettura. Vantaggi: scalabilità in lettura (load balancing delle query SELECT), disponibilità di una copia per il disaster recovery. Limite: singolo punto di scrittura (single point of failure per le scritture, salvo failover).
* **Multi-Master:** più nodi accettano scritture contemporaneamente, con meccanismi di sincronizzazione/risoluzione dei conflitti. Maggiore disponibilità in scrittura, ma complessità nella gestione della coerenza (rischio di conflitti su scritture concorrenti sullo stesso dato).
* **Replica sincrona vs asincrona:** sincrona garantisce che la scrittura sia confermata solo dopo la conferma di tutte le repliche (più sicura, più lenta); asincrona conferma subito sul master e propaga in un secondo momento (più veloce, rischio di perdita dati in caso di crash prima della propagazione).

## 3. Tuning e indicizzazione
* **Obiettivo del tuning:** ridurre i tempi di risposta delle query e l'uso di risorse (CPU, I/O, memoria).
* **Tecniche principali:**
  * Creazione di **indici mirati** sulle colonne più filtrate/ordinate (WHERE, ORDER BY, JOIN).
  * Analisi del **query plan** (EXPLAIN) per individuare full table scan evitabili.
  * **Partizionamento** delle tabelle (per range, per lista, per hash) per ridurre i dati scansionati per singola query.
  * **Connection pooling** per ridurre l'overhead di apertura/chiusura connessioni.
  * **Caching** (es. Redis) per dati letti frequentemente e poco variabili.
* **Trade-off:** troppi indici rallentano le operazioni di scrittura (INSERT/UPDATE/DELETE devono aggiornare anche gli indici) e occupano spazio aggiuntivo.

## 4. Gestione di utenze e permessi
* **Principio del privilegio minimo (Least Privilege):** ogni utente/processo deve avere solo i permessi strettamente necessari per svolgere le proprie funzioni, riducendo la superficie di attacco.
* **RBAC (Role-Based Access Control):** i permessi sono assegnati a ruoli, e gli utenti ereditano i permessi tramite l'appartenenza a un ruolo (più scalabile della gestione permesso-per-permesso).
* **Segregazione dei compiti (Separation of Duties):** funzioni critiche (es. sviluppo vs produzione, amministrazione vs audit) devono essere assegnate a persone/ruoli diversi per evitare abusi o errori non controllati.
* **Auditing degli accessi:** tracciamento di chi ha fatto cosa e quando (fondamentale per compliance GDPR e NIS2, oltre che per attività forensi in caso di incidente).

## 5. Amministrazione di sistemi Unix/Linux

### 5.1 Filesystem e permessi
* Il filesystem Unix è organizzato in un **unico albero gerarchico** con radice `/` (root); dispositivi, montaggi e risorse sono rappresentati come file (`/dev`, `/proc`, `/etc`, `/var`, `/home`).
* **Permessi (rwx):** ogni file/directory ha permessi separati per **utente proprietario (u)**, **gruppo (g)** e **altri (o)**, ciascuno con read (r=4), write (w=2), execute (x=1). Es. `chmod 750 file` → proprietario rwx, gruppo r-x, altri nessun permesso.
* **Utenti speciali:** `root` (superuser, UID 0, permessi illimitati); l'uso di `sudo` permette esecuzione di comandi privilegiati con tracciabilità (audit log), preferibile al login diretto come root.

### 5.2 Gestione processi e servizi
* **systemd:** sistema di init moderno nella maggior parte delle distribuzioni Linux; gestisce l'avvio, l'arresto e il monitoraggio dei servizi tramite **unit file** (`.service`); comandi chiave: `systemctl start/stop/status/enable <servizio>`.
* **Gestione processi:** `ps`, `top`/`htop` per monitoraggio; segnali (`kill -9` = SIGKILL forzato, `kill -15` = SIGTERM, terminazione controllata).

### 5.3 Gestione pacchetti
* **Debian/Ubuntu:** `apt` (Advanced Package Tool), pacchetti `.deb`.
* **RedHat/CentOS/Fedora:** `yum`/`dnf`, pacchetti `.rpm`.
* Le repository dei pacchetti vanno mantenute aggiornate per garantire la disponibilità di patch di sicurezza tempestive.

### 5.4 Shell scripting
* Automazione di task ripetitivi tramite script Bash: variabili, cicli (`for`, `while`), condizioni (`if`), redirezione (`>`, `>>`, `|` pipe).
* Utilizzato tipicamente per: task di backup schedulati (`cron`), deployment, monitoraggio, log rotation (`logrotate`).

### 5.5 Logging
* **syslog:** protocollo/standard per la raccolta centralizzata dei log di sistema, spesso instradato verso un sistema SIEM (Security Information and Event Management) centrale per correlazione e analisi degli incidenti.
* File di log tipici: `/var/log/auth.log` (accessi), `/var/log/syslog` o `/var/log/messages` (log di sistema generali).

## 6. Amministrazione di Windows Server

* **Active Directory (AD):** servizio di directory centralizzato per l'autenticazione e l'autorizzazione in ambiente Windows. Organizza utenti, gruppi, computer e risorse in una struttura gerarchica di **domini**, **alberi** e **foreste**. Fornisce **Single Sign-On (SSO)** all'interno del dominio.
* **Group Policy (GPO — Group Policy Object):** meccanismo per applicare configurazioni centralizzate (sicurezza, restrizioni software, impostazioni di rete) a insiemi di utenti/computer nel dominio AD, propagate automaticamente.
* **IIS (Internet Information Services):** web server nativo di Windows Server, alternativa a Apache/Nginx in ambiente Microsoft; gestisce siti, application pool (isolamento dei processi applicativi) e certificati SSL/TLS.
* **PowerShell:** shell di scripting orientata a oggetti (non solo testo, come Bash) per l'amministrazione automatizzata di Windows Server, Active Directory, Azure e altri servizi Microsoft; basata su **cmdlet** (Verbo-Sostantivo, es. `Get-Process`, `Set-ADUser`).
* **Server Manager / ruoli e feature:** interfaccia (grafica o via PowerShell) per installare e gestire ruoli del server (es. DNS, DHCP, File Server, Web Server) in modo modulare.

## 7. Hardening e patch management
* **Hardening:** insieme di pratiche per ridurre la superficie di attacco di un sistema:
  * disattivazione di servizi/porte non necessari;
  * rimozione di account di default o non utilizzati;
  * configurazione di firewall a livello host;
  * cifratura dei dati a riposo (at rest) e in transito (in transit);
  * segmentazione di rete (VLAN, zone DMZ) per isolare sistemi critici.
* **Patch management:** processo strutturato di identificazione, test e applicazione tempestiva degli aggiornamenti di sicurezza, per chiudere le vulnerabilità note (CVE) prima che vengano sfruttate. Un ritardo nel patching è una delle cause più comuni di incidenti di sicurezza.
* **Logging e audit:** raccolta e conservazione sicura (integrità, non ripudio) dei log di accesso e delle operazioni privilegiate, requisito richiamato anche dalla normativa NIS2 per la rilevazione tempestiva di incidenti.

---

## Domande di autoverifica

1. **Quale tipo di backup richiede solo l'ultimo full e l'ultimo backup stesso per il ripristino, senza dover applicare una catena di file intermedi?**
   a) Incrementale b) **Differenziale** c) Full giornaliero d) Snapshot — corretto: il differenziale salva sempre le modifiche rispetto all'ultimo full, quindi basta un solo file oltre al full.

2. **In una replica master-slave, cosa accade tipicamente alle query di sola lettura in un'architettura ben progettata?**
   a) Vengono sempre indirizzate al master b) **Possono essere distribuite sugli slave per bilanciare il carico** c) Non sono supportate d) Bloccano le scritture sul master — corretto: uno dei principali vantaggi della replica master-slave è la scalabilità in lettura tramite gli slave.

3. **Il comando `chmod 640 file` assegna quali permessi?**
   a) rwx per tutti b) **rw- al proprietario, r-- al gruppo, nessun permesso agli altri** c) r-- al proprietario, rw- al gruppo, x agli altri d) rwx solo al proprietario — corretto: 6=rw-, 4=r--, 0=---.

4. **Qual è la funzione principale di una Group Policy in Active Directory?**
   a) Sostituire il DNS del dominio b) **Applicare centralmente configurazioni di sicurezza/sistema a utenti e computer del dominio** c) Gestire i backup dei database d) Compilare gli script PowerShell — corretto: le GPO propagano impostazioni centralizzate su larga scala nel dominio.

5. **Perché un numero eccessivo di indici su una tabella può essere controproducente?**
   a) Non ha alcun effetto negativo b) Rallenta solo le query SELECT c) **Rallenta le operazioni di scrittura (INSERT/UPDATE/DELETE) perché ogni indice va aggiornato, oltre a occupare spazio** d) Impedisce l'uso di JOIN — corretto: gli indici velocizzano le letture ma hanno un costo di mantenimento sulle scritture.

6. **Cosa garantisce un backup "immutabile" (WORM)?**
   a) Viene compresso automaticamente b) **Non può essere modificato o cancellato per un periodo definito, proteggendo da attacchi ransomware** c) È sempre incrementale d) Sostituisce la necessità di test di restore — corretto: l'immutabilità impedisce la cifratura/cancellazione del backup da parte di un attaccante che ha compromesso il sistema.
