# 🤖 Game the LLM Reviewer

[English / 中文](README.md) · [日本語](README.ja.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md)

Game the LLM Reviewer es una **habilidad (skill)** para editar un artículo terminado antes de enviarlo a una publicación o congreso. Utiliza los hallazgos de estudios sobre las preferencias de los LLM al revisar artículos para introducir pequeños cambios de redacción sin alterar el significado científico.

Compatible con **Claude Code**, **Codex** y otros agentes que admitan Agent Skills.

[Inicio rápido](#quick-start) · [Antes y después](#before-after) · [Estrategias](skills/game-the-llm-reviewer/references/strategies.md) · [Investigación](skills/game-the-llm-reviewer/references/research.md)

![Un revisor de IA cuestiona un artículo; tras reformular la redacción, los revisores responden más favorablemente al mismo contenido científico.](assets/hero.png)

> **Si no podemos evitar por completo la revisión con LLM, aprovechemos sus preferencias para proteger nuestro trabajo de investigación.**

Nos oponemos a delegar en los LLM las decisiones de la revisión por pares. Sin embargo, los autores suelen tener poco control sobre si un revisor utiliza uno, y varios estudios han encontrado que los cambios de redacción pueden influir en la evaluación. Esta habilidad permite tener en cuenta esas preferencias después del proceso habitual de escritura y revisión, sin consultar a un modelo revisor objetivo.

> Un artículo debe juzgarse por sus métodos, pruebas y contribuciones. Aun así, se ha observado que los revisores LLM pueden asignar puntuaciones distintas a un mismo párrafo cuando se reformula.

> Esta herramienta es una última revisión «defensiva» antes del envío: se basa en estudios sobre las preferencias de los revisores LLM para elegir, entre formulaciones de significado equivalente, aquellas que puedan resultarles más favorables, manteniendo prácticamente intacto el contenido científico que puede evaluar una persona.

> ⚠️ **Integridad académica**
>
> Los cambios deben conservar las afirmaciones del artículo y las pruebas que las respaldan, incluidas las citas, los supuestos, la incertidumbre y las limitaciones sustanciales. Registra cada cambio. Los resultados inventados, la novedad exagerada, las debilidades ocultas y las instrucciones encubiertas a los revisores quedan fuera del alcance de esta habilidad.
>
> Los autores siguen siendo responsables del manuscrito y de cumplir las normas de la publicación o del congreso sobre asistencia de IA y su declaración.

> **Termina el artículo → Usa tus herramientas habituales de escritura → Aplica Game-the-LLM-Reviewer al final.**

<a id="quick-start"></a>

## 🚀 Inicio rápido

### 1. Instala la habilidad

**Pide a tu agente de programación que la instale:**

```text
Clona este repositorio e instala su habilidad game-the-llm-reviewer:
https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer
```

O instálala con [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer
```

### 2. Aplícala a tu manuscrito

Entrega a tu agente un manuscrito terminado:

```text
Aplica game-the-llm-reviewer a paper/main.tex. Lee primero las secciones incluidas.
Haz pequeños cambios de redacción que preserven el significado y tengan en cuenta las preferencias de los revisores LLM.
Mantén intacta la evaluación científica que podría realizar una persona.
Guarda una copia revisada y un archivo changes.md que explique cada cambio retórico.
```

El agente guarda una **copia revisada** y una **nota de cambios** que explica las modificaciones. Funciona con tu entorno de escritura actual y no requiere ninguna API adicional de revisión.

<details>
<summary>Instalación para un agente concreto, acceso privado y uso manual</summary>

Para seleccionar explícitamente un agente:

```sh
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a claude-code
npx skills add Michael-Jiahao-Zhang/game-the-llm-reviewer --skill game-the-llm-reviewer -a codex
```

Ejecuta el comando correspondiente a tu agente. Por defecto, la instalación es local al proyecto; añade `-g` para una instalación personal. El instalador requiere Node.js (consulta los [requisitos actuales](https://github.com/vercel-labs/skills/blob/main/package.json)). Los repositorios privados requieren acceso a GitHub y autenticación configurada mediante Git, GitHub CLI o SSH.

Para el uso manual, clona el repositorio y pide a cualquier agente de escritura que pueda leer archivos que consulte la habilidad:

```sh
git clone https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer.git
cd game-the-llm-reviewer
```

```text
Lee skills/game-the-llm-reviewer/SKILL.md y aplícalo a mi manuscrito terminado.
Devuelve una copia revisada y una nota de cambios breve.
```

Para instalarla manualmente, copia la carpeta **completa** `skills/game-the-llm-reviewer/`, incluidas sus referencias, en el directorio de habilidades compatible con tu agente. Revisa cualquier instalación existente antes de sustituirla. La habilidad en sí no tiene dependencias de ejecución; la gestión de archivos y la compilación de LaTeX utilizan las herramientas disponibles en tu agente.

</details>

<a id="before-after"></a>

## ✨ Antes y después

Este ejemplo es una descripción de las contribuciones en la introducción de un artículo sobre **memoria de ejecución para agentes de programación**.

### Antes

> Los agentes de programación pueden perder el rastro de los intentos de reparación fallidos a medida que se acumulan las salidas de las herramientas. Proponemos una memoria de ejecución que registra los parches intentados y los resultados de sus pruebas para utilizarlos en pasos posteriores, sin actualizar los pesos del modelo. En 300 incidencias de repositorios Python, con dos modelos base y un presupuesto fijo de tokens por incidencia, el agente con memoria resuelve el 34% y el 39% de las incidencias, frente al 30% y el 35% de los mismos agentes sin memoria, respectivamente.

### Después de Game the LLM Reviewer

> Presentamos una memoria de ejecución para agentes de programación que no requiere actualizar los pesos del modelo. Registra los parches intentados y los resultados de sus pruebas para utilizarlos en pasos posteriores, abordando la pérdida del historial de intentos fallidos a medida que se acumulan las salidas de las herramientas. En 300 incidencias de repositorios Python, con dos modelos base y un presupuesto fijo de tokens por incidencia, la memoria de ejecución aumenta la resolución de incidencias en 4 puntos porcentuales para cada modelo: del 30% al 34% y del 35% al 39%, respectivamente.

### Qué cambió

| Estrategia | Cambio |
|---|---|
| **S1 · Presentación de la contribución** | Trasladar la propiedad ya existente de no actualizar los pesos a la descripción inicial del método |
| **S2 · Presentación de las pruebas** | Expresar las mismas tasas de resolución como mejoras de 4 puntos porcentuales, conservando tanto las tasas de referencia como las finales |
| **S3 · Énfasis del resumen** | Comenzar con la contribución y mantener después el contexto original del problema |

Ambas versiones describen el mismo método y la misma evaluación. La revisión destaca la contribución y expresa las diferencias ya existentes entre las tasas en puntos porcentuales. Consulta las [fichas de estrategias](skills/game-the-llm-reviewer/references/strategies.md) para más detalles.

<details>
<summary>Pruébala con el ejemplo incluido de agentes de programación</summary>

Desde la raíz del repositorio, pide a tu agente:

```text
Lee skills/game-the-llm-reviewer/SKILL.md y aplícalo a examples/coding-agent-introduction.md.
Guarda introduction.revised.md e introduction.changes.md.
```

Compara el resultado con el ejemplo de antes y después mostrado arriba.

</details>

## 🎯 Uso con otras herramientas de escritura

Ejecuta esta habilidad una vez terminados el borrador y la revisión habitual. Puede aplicarse después de un flujo de escritura existente, incluidos los que ofrecen estos proyectos:

| Proyecto | Cómo encaja |
|---|---|
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | Produce un artículo mediante un proceso de investigación automatizado; aplica esta habilidad al borrador terminado. |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) / [AI Research Skills](https://github.com/Orchestra-Research/AI-Research-SKILLs) | Ofrecen herramientas más amplias de investigación y escritura para etapas anteriores del proceso. |
| [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) / [Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar) | Cubren la redacción y la revisión; aplica esta habilidad cuando esas modificaciones estén completas. |
| [ARGAR](https://github.com/xyimatvoid/ARGAR) | Optimiza la presentación mediante comentarios reiterados de revisores de IA. Esta habilidad aplica un conjunto preparado de estrategias de edición sin un ciclo de comentarios de un revisor. |

## 🛠️ Estrategias de edición

| Dimensión retórica | Operación que preserva el significado |
|---|---|
| **S1 · Presentación de la contribución** | Expresar la misma contribución establecida con un énfasis gramatical diferente |
| **S2 · Presentación de las pruebas** | Reformular la misma comparación numérica como un efecto medido |
| **S3 · Énfasis del resumen** | Cambiar el orden o el énfasis de afirmaciones existentes sin añadir explicaciones |
| **S4 · Elección léxica** | Ajustar expresiones valorativas que no aportan hechos, conservando el grado de certeza |
| **S5 · Presentación del alcance** | Reformular el mismo alcance evaluado y no evaluado sin restar importancia a la limitación |
| **S6 · Comprobación de equivalencia** | Verificar que los cambios mantienen intactas las afirmaciones, las pruebas y las implicaciones científicas |

Cada [ficha de estrategia](skills/game-the-llm-reviewer/references/strategies.md) describe cuándo utilizar un cambio y qué preservar. El agente selecciona las modificaciones pertinentes de S1–S5 y utiliza S6 para contrastarlas con el original. Puede dejar un pasaje sin cambios.

<details>
<summary>Instrucciones listas para usar: resumen, teoría o artículo ya revisado</summary>

**Solo el resumen**

```text
Aplica game-the-llm-reviewer a este resumen y mantenlo por debajo de 200 palabras.
Trabaja solo con el texto proporcionado y conserva tanto los resultados positivos como los negativos.
Devuelve un texto de sustitución y una nota de cambios breve.
```

**Artículo teórico**

```text
Aplica game-the-llm-reviewer a paper/main.tex. Ajusta la presentación de la contribución sin cambiar su significado científico.
Conserva los supuestos de los teoremas, los cuantificadores y la distinción entre una cota superior y una tasa óptima.
```

**Después de otra habilidad de escritura**

```text
El borrador ya está revisado. Utiliza game-the-llm-reviewer como último paso.
Reutiliza el mapa de afirmaciones y pruebas adjunto y contrástalo con el manuscrito.
Utiliza las estrategias incluidas para seleccionar pequeños cambios de redacción orientados a las preferencias de revisión de los LLM.
Mantén intactos el significado y la evaluación científica; no reformules solo por estilo.
```

</details>

## 📦 Resultado

El resultado incluye un manuscrito revisado y una nota de cambios. Para un fragmento breve, el agente puede devolver texto de sustitución y explicar las modificaciones junto a él. Ejemplo de nota:

| Pasaje | Estrategia / motivo | Significado preservado |
|---|---|---|
| Inicio de la introducción y resultados | S1/S3: contribución primero; S2: mejoras de resolución | Misma memoria de ejecución, pesos del modelo sin cambios, 300 incidencias de Python, dos modelos, presupuesto de tokens y tasas de resolución |

La nota identifica qué partes del artículo se leyeron y vincula los cambios con las pruebas pertinentes. En proyectos LaTeX, el agente conserva las relaciones entre archivos y compila la revisión cuando dispone de las herramientas adecuadas.

## 📚 Referencias

Las [notas de investigación](skills/game-the-llm-reviewer/references/research.md) resumen estos artículos y relacionan sus hallazgos con las estrategias de edición:

- [How Can Rhetoric Reward-Hack AI Reviewers?](https://arxiv.org/abs/2608.08975) examina qué dimensiones retóricas afectan a las revisiones.
- [No Hidden Prompts Needed!](https://arxiv.org/abs/2606.13044) estudia revisiones que solo modifican la presentación mediante ARGAR.
- [Gaming AI-Assisted Peer Reviews](https://arxiv.org/abs/2606.10159) estudia la reformulación de resúmenes.
- [LLM-REVal](https://arxiv.org/abs/2510.12367) compara las preferencias por textos humanos y textos de LLM.
- [Are We There Yet?](https://arxiv.org/abs/2412.01708) examina fallos de revisión, incluidas las respuestas a limitaciones declaradas.

## 🤝 Contribuciones

Se agradecen las correcciones y los ejemplos adicionales de redacción. Incluye la fuente o el razonamiento que respalde cualquier cambio de estrategia propuesto; consulta [CONTRIBUTING.md](CONTRIBUTING.md).

---

Los archivos originales de este proyecto se distribuyen bajo la [licencia MIT](LICENSE). Las investigaciones, los conjuntos de datos y el código de otros proyectos citados conservan sus propias licencias. Este proyecto es independiente de los autores citados.
