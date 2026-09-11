# mermaid-display-app

A local Flask viewer/editor for Mermaid `.mmd` files, including master diagrams assembled with `%% INCLUDE` directives.

## Run

    python3 -m pip install -r requirements.txt
    python3 app.py

Open the application on port 5012.

## Editable PowerPoint export

Open a diagram in the viewer and click **Export editable PPTX**. The app first resolves any `%% INCLUDE` files, then uses `diagram-pptx` with `python-pptx` to generate a 16:9 PowerPoint slide containing native editable shapes, connectors and text rather than a screenshot.

Flowchart, sequence, class, ER and state diagrams use the package's pure-Python native renderer. Other Mermaid families may require Mermaid CLI/Official rendering support.
