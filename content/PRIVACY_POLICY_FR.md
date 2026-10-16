# PoolPilot — Politique de confidentialité (projet français)

**À vérifier avant publication :** cohérence avec la version distribuée, déclarations App Privacy, mentions d'immatriculation et d'hébergement, puis URL publique effective. Ce texte décrit la version 1 auditée le 16 octobre 2026. Il n'est pas encore une politique publiée.

## Qui contacter

PoolPilot est édité par **Arnaud Mourcel, entrepreneur individuel (EI), micro-entrepreneur**, 244 rue de Bègles, 33800 Bordeaux, France. Contact : **arnaudmourcel47@gmail.com** ; téléphone : **06 45 48 02 03**. Les professionnels qui utilisent PoolPilot saisissent des informations sur leurs propres clients et doivent les gérer conformément à leurs obligations applicables. L'éditeur n'a pas d'accès distant aux dossiers stockés uniquement dans l'application ; le professionnel reste responsable de l'utilisation des coordonnées de ses propres clients.

## Informations utilisées

L'application permet d'enregistrer des coordonnées et adresses de clients, des notes, des informations de piscines et d'équipements, des rendez-vous, interventions, mesures d'eau, produits utilisés, opérations de maintenance, photos, ainsi qu'un profil d'entreprise et son logo. Ces informations sont saisies ou choisies par l'utilisateur. PoolPilot n'exige pas la création d'un compte utilisateur.

Les réglages de l'application, les rappels et les informations d'état d'abonnement nécessaires à l'affichage des droits sont également utilisés. PoolPilot n'accède qu'aux images sélectionnées par l'utilisateur dans le sélecteur Photos d'Apple ; aucune autorisation d'accès général à la photothèque n'est demandée par les parcours audités.

## Stockage et utilisation

Les dossiers professionnels sont conservés dans le stockage local de l'application sur l'appareil, au moyen de SwiftData et de fichiers dans Application Support. Les images enregistrées sont réduites puis stockées comme fichiers ; les modèles de données ne conservent que leurs chemins relatifs. Les informations servent à afficher et modifier les dossiers, organiser les tournées, créer des rappels et générer des rapports PDF.

La version 1 auditée n'utilise pas CloudKit pour synchroniser les dossiers. L'audit du code n'a pas trouvé de serveur exploité par l'éditeur, de SDK publicitaire ni d'outil d'analyse intégré à la cible commerciale. Ce constat technique ne remplace pas la vérification finale des déclarations **App Privacy** et des services effectivement activés au moment de la distribution. Les sauvegardes de l'appareil gérées par iOS peuvent, selon les réglages de l'utilisateur, contenir des données de l'application ; elles sont distinctes d'une synchronisation CloudKit de PoolPilot.

## Services Apple et actions choisies par l'utilisateur

- **Photos :** l'utilisateur sélectionne les images à importer. Les copies de travail de PoolPilot sont stockées localement.
- **Notifications locales :** si l'utilisateur les autorise, PoolPilot programme des rappels de maintenance sur l'appareil. Leur texte peut contenir le nom d'une piscine ou une tâche et apparaître sur l'écran verrouillé selon les réglages iOS.
- **Plans, téléphone et email :** l'ouverture d'un itinéraire transmet l'adresse choisie à Apple Plans ; les boutons d'appel et d'email ouvrent les applications correspondantes avec les coordonnées sélectionnées. Leur utilisation est régie par les réglages et politiques de ces services.
- **Abonnements :** les produits, achats et droits sont fournis et vérifiés par Apple via StoreKit. PoolPilot ne reçoit pas les numéros de carte bancaire. Aucune transaction non vérifiée n'accorde un droit Pro.
- **Partage :** un PDF ou une sauvegarde ne quitte l'application que si l'utilisateur choisit une destination dans la feuille de partage iOS ou Fichiers. Cette destination, éventuellement iCloud Drive, est alors soumise à sa propre politique.

## Sauvegardes, sécurité et conservation

Les archives manuelles `.poolpilotbackup` contiennent des dossiers et photos professionnels. **Elles ne sont pas chiffrées par PoolPilot.** L'utilisateur doit les conserver dans un emplacement sûr et contrôler à qui il les transmet. PoolPilot vérifie leur intégrité avant de proposer une restauration. Une restauration peut conserver une génération locale précédente pour permettre un retour arrière. Les PDF et archives exportés sont préparés dans des dossiers temporaires et font l'objet d'un nettoyage applicatif ; toute copie enregistrée ou partagée ailleurs reste sous le contrôle du service ou de la personne destinataire.

Les données restent sur l'appareil jusqu'à leur modification ou suppression par l'utilisateur, une restauration choisie, ou la suppression de l'application et de ses données par iOS. Certaines opérations conservent un historique professionnel ; supprimer un client ne signifie pas nécessairement supprimer les piscines et interventions liées. Les copies externes et sauvegardes système doivent être gérées séparément.

## Choix et demandes

L'utilisateur peut consulter ses dossiers et exporter une sauvegarde même si son abonnement Pro a expiré. Il peut modifier ou supprimer les éléments pour lesquels l'interface prévoit cette action. L'éditeur ne dispose pas d'un accès à distance aux dossiers stockés uniquement sur l'appareil ; une demande adressée à l'éditeur ne peut donc pas, à elle seule, effacer une copie locale ou une archive partagée. Pour toute question sur les données ou l'exercice de droits applicables, écrire à **arnaudmourcel47@gmail.com**.

Selon les conditions applicables, les personnes concernées peuvent demander l'accès, la rectification, l'effacement ou la limitation du traitement de leurs données, ainsi que s'opposer au traitement ou demander la portabilité lorsque ces droits s'appliquent. Pour des données de clients conservées uniquement par un professionnel dans son appareil, contacter d'abord ce professionnel : l'éditeur ne peut pas consulter ni modifier ces dossiers à distance. Une réclamation peut être adressée à la **CNIL** via [cnil.fr](https://www.cnil.fr/fr/plaintes).

## Consultation du site public

Le site d'information PoolPilot est prévu sur **GitHub Pages**. Le code du site ne contient ni formulaire, ni outil d'analyse, ni script publicitaire, ni ressource chargée depuis un réseau tiers. La consultation d'une page entraîne toutefois une connexion aux serveurs de GitHub, qui peuvent traiter des données techniques de connexion selon leur [politique de confidentialité](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). L'éditeur n'utilise pas ces données pour suivre les visiteurs du site. Les liens vers d'autres services ouvrent ces services à la demande du visiteur.

Si un visiteur écrit à **arnaudmourcel47@gmail.com**, son adresse électronique et le contenu de son message servent à répondre à sa demande et, si nécessaire, à suivre l'assistance. La réponse aux demandes d'assistance repose sur l'intérêt légitime de l'éditeur à assurer ce service ; une demande d'exercice de droits est traitée pour respecter les obligations légales applicables. Ces échanges sont accessibles à l'éditeur et transitent par **Gmail (Google)**. Selon la [documentation de Google](https://policies.google.com/privacy/frameworks?hl=fr), des données peuvent être traitées hors de l'Espace économique européen ; les garanties applicables doivent être vérifiées avant publication. L'éditeur prévoit de supprimer les messages d'assistance au plus tard **12 mois après le dernier échange**, sauf obligation légale ou nécessité documentée de conserver un échange lié à un litige. Cette règle doit être appliquée effectivement à la boîte mail et réévaluée si les pratiques changent. Aucun formulaire de contact n'est intégré au site.

Cette politique doit être revue si des fonctions, intégrations ou pratiques de traitement changent. URL publique prévue : **https://arnaudmourcel47-spec.github.io/poolpilot-site/privacy/** (à vérifier après activation). Date d'entrée en vigueur prévue : **16 octobre 2026** (date communiquée par l'éditeur ; publication non encore effectuée).
