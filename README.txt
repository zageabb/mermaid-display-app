# mermaid-display-app

## Ubuntu server deployment

Verified on **14 September 2026** against the listeners, user systemd services,
Docker port mappings and deployment registry on `192.168.1.249`.

The registered service name refers to this project, but the active systemd
override runs **[mermaid_final](https://github.com/zageabb/mermaid_final)** from
`/home/zageabb/mermaid/mermaid_final` on **5070**. This checkout is not the
code directory used by that running service. Open [the active Mermaid app](http://192.168.1.249:5070/).

Checkout: `/home/zageabb/flask/mermaid-display-app`.

These are **user** systemd units. Inspect them with:

```bash
systemctl --user status migrated-flask@mermaid-display-app.service
systemctl --user cat migrated-flask@mermaid-display-app.service
```

Local verification URL: `http://127.0.0.1:5070/`. HTTP 200 was observed during this audit.

Development defaults and container-internal ports elsewhere in this repository
may differ from this host deployment. Use the live ports above when accessing
this Ubuntu server; do not start a second copy on a port already occupied.

[Complete Ubuntu port inventory](https://github.com/zageabb/universal-deployment-agent/blob/main/UBUNTU_PORTS.md).

A local Flask viewer/editor for Mermaid `.mmd` files, including master diagrams assembled with `%% INCLUDE` directives.

## Run

    python3 -m pip install -r requirements.txt
    python3 app.py

The standalone development instructions use port 5012. The active Ubuntu service runs mermaid_final on port 5070; see the deployment note above.

## Editable PowerPoint export

Open a diagram in the viewer and click **Export editable PPTX**. The app first resolves any `%% INCLUDE` files, then uses `diagram-pptx` with `python-pptx` to generate a 16:9 PowerPoint slide containing native editable shapes, connectors and text rather than a screenshot.

Flowchart, sequence, class, ER and state diagrams use the package's pure-Python native renderer. Other Mermaid families may require Mermaid CLI/Official rendering support.
