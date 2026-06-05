# Vehicle Infographics — Blueprint Style

- Type: prompt-template
- Lifecycle status: captured
- Applies To: image generation for vehicle infographics
- Trigger: when a transport object needs to be shown as a technical infographic with blueprint-style overlays
- Source: adapted from a social prompt example shared by the owner; wording cleaned up and normalized for reuse

## Purpose

Reusable prompt template for generating infographic-style images of vehicles, aircraft, motorcycles, vans, and other transport objects using a real-photo base plus blueprint-style technical overlays.

## Important Correction

The original shared version used the word `landmark`, which does not match the actual use case.
For this reusable prompt entry, it is corrected to `vehicle`.

## Variables

- `[VEHICLE]` = the specific vehicle or transport object name
- Optional language instruction = `All labels and annotations must be in Russian.`

## Full Version — English

"Create an infographic image of [VEHICLE], combining a real photograph of the vehicle with blueprint-style technical annotations and diagrams overlaid on the image. Include the title \"[VEHICLE]\" in a hand-drawn box in the corner. Add white chalk-style sketches showing key structural data, important measurements, material quantities, internal diagrams, load-flow arrows, cross-sections, floor plans, and notable engineering features. Style: blueprint aesthetic with white line drawings on the photograph, technical/architectural annotation style, educational infographic feel, with the real environment visible behind the annotations. 1:1 dimension."

## Full Version — Russian Translation

«Создай инфографическое изображение [ТРАНСПОРТНОГО СРЕДСТВА], объединив реальную фотографию этого транспортного средства с наложенными поверх неё техническими аннотациями и схемами в стиле чертежа. Добавь в углу заголовок \"[ТРАНСПОРТНОЕ СРЕДСТВО]\" в нарисованной от руки рамке. Наложи белые эскизы в меловом стиле, показывающие ключевые конструктивные данные, важные размеры, количество материалов, внутренние схемы, стрелки распределения нагрузок, поперечные сечения, планы сверху и другие заметные инженерные особенности. Стиль: эстетика blueprint, белые линейные чертежи поверх фотографии, технический/архитектурный стиль аннотаций, образовательный формат инфографики, при этом реальное окружение должно оставаться видимым на фоне. Формат: 1:1.»

## Short Version — English

"Create a square 1:1 infographic of [VEHICLE] using a real photo as the base. Overlay blueprint-style white technical sketches and annotations showing dimensions, materials, internal structure, cross-sections, top views, load-flow arrows, and key engineering features. Put the title \"[VEHICLE]\" in a hand-drawn box in the corner. Keep the real environment visible behind the technical overlays."

## Short Version — Russian Translation

«Создай квадратную инфографику 1:1 с [ТРАНСПОРТНЫМ СРЕДСТВОМ], используя реальную фотографию как основу. Поверх фотографии добавь белые технические схемы и аннотации в стиле blueprint, показывающие размеры, материалы, внутреннее устройство, поперечные сечения, вид сверху, стрелки нагрузок и ключевые инженерные особенности. В углу размести заголовок \"[ТРАНСПОРТНОЕ СРЕДСТВО]\" в нарисованной от руки рамке. Сохрани видимость реального окружения за техническими наложениями.»

## Recommended Russian-Output Add-On

English:
"All labels, annotations, and technical callouts must be in Russian."

Russian:
«Все подписи, аннотации и технические выноски должны быть на русском языке.»

## Usage Notes

- Replace `[VEHICLE]` with the exact object name, for example: `Boeing 747`, `Ford Transit`, `Batmobile`, `Kaneda Bike`.
- If Russian output is required, add the Russian-output instruction explicitly.
- If needed, expand the prompt with domain-specific details such as armor layout, cabin layout, payload, propulsion, or suspension.

## Review Status

Captured for future reuse. Not yet reviewed as an active standard.
