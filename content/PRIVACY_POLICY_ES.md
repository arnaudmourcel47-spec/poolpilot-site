# PoolPilot — Política de privacidad

Esta política describe PoolPilot versión 1 y este sitio web. **Fecha de entrada en vigor: 16 de octubre de 2026. Última actualización: 24 de octubre de 2026.**

## Contacto

PoolPilot es publicado por **Arnaud Mourcel, empresario individual francés (entrepreneur individuel, EI) y microempresario**, 244 rue de Bègles, 33800 Bordeaux, Francia. Contacto: **arnaudmourcel47@gmail.com**; teléfono: **06 45 48 02 03**. Los profesionales que utilizan PoolPilot introducen información de sus propios clientes y deben gestionarla conforme a sus obligaciones aplicables. El editor no tiene acceso remoto a los expedientes guardados únicamente en la app; el profesional sigue siendo responsable del uso de los datos de contacto de sus propios clientes.

## Información utilizada

La aplicación permite guardar datos de contacto y direcciones de clientes, notas, información de piscinas y equipos, citas, intervenciones, mediciones del agua, productos utilizados, tareas de mantenimiento, fotografías y el perfil de la empresa con su logotipo. El usuario introduce o selecciona esta información. PoolPilot no exige crear una cuenta dentro de la aplicación.

También se utilizan los ajustes de la aplicación, la información de recordatorios locales y el estado de la suscripción necesario para mostrar los permisos de acceso. En los flujos revisados, PoolPilot recibe únicamente las imágenes seleccionadas mediante el selector Fotos de Apple; no solicita acceso general a la fototeca.

## Almacenamiento y finalidad

Los expedientes profesionales permanecen en el almacenamiento local de la aplicación en el dispositivo, mediante SwiftData y archivos en Application Support. Las imágenes importadas se reducen y se guardan como archivos; los modelos de datos conservan solo rutas relativas. La información sirve para consultar y modificar expedientes, planificar recorridos, programar recordatorios y generar informes PDF.

La versión 1 no utiliza CloudKit para sincronizar expedientes. La auditoría del código no encontró servidores gestionados por el editor, SDK publicitarios ni SDK de análisis integrados en la aplicación comercial. Las copias de seguridad del dispositivo gestionadas por iOS pueden incluir datos de la aplicación según los ajustes del usuario; son distintas de la sincronización CloudKit de PoolPilot.

## Servicios Apple y acciones iniciadas por el usuario

- **Fotos:** el usuario elige las imágenes que importa. Las copias de trabajo de PoolPilot se guardan localmente.
- **Notificaciones locales:** con permiso, PoolPilot programa recordatorios de mantenimiento en el dispositivo. Su texto puede incluir el nombre de una piscina o una tarea y aparecer en la pantalla bloqueada según los ajustes de iOS.
- **Mapas, teléfono y correo:** al abrir una ruta se envía la dirección elegida a Apple Maps; las acciones de llamada y correo abren las aplicaciones correspondientes con los datos seleccionados. Estos servicios se rigen por sus propios ajustes y políticas.
- **Suscripciones:** Apple proporciona y verifica productos, compras y derechos de acceso mediante StoreKit. PoolPilot no recibe números de tarjetas bancarias. Una transacción no verificada no concede acceso Pro.
- **Compartir:** un PDF o una copia de seguridad sale de la aplicación únicamente si el usuario elige un destino en la hoja para compartir de iOS o en Archivos. Ese destino, que puede ser iCloud Drive, tiene su propia política.

## Copias de seguridad, seguridad y conservación

Los archivos manuales `.poolpilotbackup` contienen expedientes y fotografías profesionales. **PoolPilot no cifra estos archivos.** El usuario debe guardarlos en un lugar seguro y controlar con quién los comparte. PoolPilot comprueba su integridad antes de ofrecer la restauración. Una restauración puede conservar una generación local anterior para permitir la reversión. Los PDF y archivos exportados se preparan en carpetas temporales y se someten a limpieza en la aplicación; las copias guardadas o compartidas en otros lugares quedan bajo el control de su destino o destinatario.

Los datos permanecen en el dispositivo hasta que el usuario los modifica o elimina, elige una restauración o borra la aplicación y sus datos mediante iOS. Algunas operaciones conservan el historial profesional: eliminar un cliente no implica necesariamente eliminar sus piscinas e intervenciones. Las copias externas y las copias de seguridad del sistema deben gestionarse por separado.

## Opciones y solicitudes

El usuario puede consultar sus expedientes y exportar una copia de seguridad aunque caduque su suscripción Pro. Puede modificar o eliminar los elementos para los que la interfaz ofrece esa acción. El editor no tiene acceso remoto a los expedientes almacenados solo en el dispositivo; por ello, contactar con el editor no puede, por sí solo, borrar una copia local ni un archivo compartido. Para consultas sobre los datos o el ejercicio de derechos aplicables: **arnaudmourcel47@gmail.com**.

Cuando corresponda, las personas interesadas pueden solicitar acceso, rectificación, supresión o limitación del tratamiento de sus datos personales, así como oponerse al tratamiento o solicitar la portabilidad si esos derechos son aplicables. Para los expedientes de clientes guardados únicamente por un profesional en su dispositivo, hay que contactar primero con ese profesional: el editor no puede consultar ni modificar dichos expedientes a distancia. Se puede presentar una reclamación ante la **CNIL** en [cnil.fr](https://www.cnil.fr/fr/plaintes).

## Visita al sitio público

El sitio informativo de PoolPilot está alojado en **GitHub Pages**. Su código no contiene formularios de contacto, herramientas de análisis, scripts publicitarios ni recursos cargados desde redes de terceros. No obstante, visitar una página conecta el navegador con los servidores de GitHub, que pueden tratar datos técnicos de conexión conforme a su [política de privacidad](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). El editor no utiliza esos datos para seguir a los visitantes del sitio. Los enlaces externos abren otros servicios a petición del visitante.

Si un visitante escribe a **arnaudmourcel47@gmail.com**, su dirección de correo, el contenido del mensaje y los archivos adjuntos que envíe se utilizan para responder y, cuando sea necesario, dar seguimiento a la asistencia. La gestión de solicitudes de asistencia se basa en el interés legítimo del editor de prestar este servicio; las solicitudes de ejercicio de derechos se tramitan para cumplir las obligaciones legales aplicables. El editor puede acceder a la correspondencia, que pasa por **Gmail (Google)**. Según la [documentación de Google](https://policies.google.com/privacy/frameworks?hl=es), los datos pueden tratarse fuera del Espacio Económico Europeo. El editor prevé eliminar los mensajes de asistencia **a más tardar 12 meses después del último intercambio**, salvo obligación legal o necesidad documentada de conservar un intercambio por un litigio. El sitio no tiene formulario de contacto.

Esta política se actualizará si cambian las funciones, integraciones o prácticas de tratamiento. Está disponible en **https://arnaudmourcel47-spec.github.io/poolpilot-site/es/privacy/**.
