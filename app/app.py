from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Internship Dashboard</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
        }

        .container {
            max-width: 1100px;
            margin: auto;
            padding: 45px 25px;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 35px;
        }

        h1 {
            margin: 0;
            font-size: 30px;
        }

        .subtitle {
            color: #94a3b8;
            margin-top: 8px;
        }

        .status {
            background: #052e16;
            color: #4ade80;
            border: 1px solid #166534;
            padding: 10px 16px;
            border-radius: 20px;
            font-size: 14px;
        }

        h2 {
            font-size: 18px;
            margin-top: 30px;
            margin-bottom: 15px;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
        }

        .card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 10px;
            padding: 20px;
        }

        .card h3 {
            margin-top: 0;
            margin-bottom: 15px;
            font-size: 16px;
        }

        .healthy {
            color: #4ade80;
            font-weight: bold;
        }

        .dot {
            display: inline-block;
            width: 9px;
            height: 9px;
            background: #22c55e;
            border-radius: 50%;
            margin-right: 7px;
        }

        .info {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 10px;
            overflow: hidden;
        }

        .row {
            display: flex;
            justify-content: space-between;
            padding: 14px 20px;
            border-bottom: 1px solid #334155;
        }

        .row:last-child {
            border-bottom: none;
        }

        .label {
            color: #94a3b8;
        }

        footer {
            margin-top: 35px;
            color: #64748b;
            font-size: 13px;
            text-align: center;
        }

        @media (max-width: 700px) {
            .services {
                grid-template-columns: 1fr;
            }

            header {
                display: block;
            }

            .status {
                display: inline-block;
                margin-top: 20px;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <header>
        <div>
            <h1>DevOps Internship Dashboard</h1>
            <div class="subtitle">
                Development Environment • Service Overview
            </div>
        </div>

        <div class="status">
            ● System Operational
        </div>
    </header>


    <h2>Service Overview</h2>

    <div class="services">

        <div class="card">
            <h3>Web Application</h3>
            <div class="healthy">
                <span class="dot"></span>Running
            </div>
        </div>

        <div class="card">
            <h3>Nginx Reverse Proxy</h3>
            <div class="healthy">
                <span class="dot"></span>Active
            </div>
        </div>

        <div class="card">
            <h3>Monitoring</h3>
            <div class="healthy">
                <span class="dot"></span>Connected
            </div>
        </div>

    </div>


    <h2>Application Information</h2>

    <div class="info">

        <div class="row">
            <span class="label">Service</span>
            <span>internship-app</span>
        </div>

        <div class="row">
            <span class="label">Environment</span>
            <span>Development</span>
        </div>

        <div class="row">
            <span class="label">Version</span>
            <span>1.0.0</span>
        </div>

        <div class="row">
            <span class="label">Container Platform</span>
            <span>Docker</span>
        </div>

        <div class="row">
            <span class="label">Reverse Proxy</span>
            <span>Nginx</span>
        </div>

        <div class="row">
            <span class="label">Monitoring</span>
            <span>Prometheus / Grafana</span>
        </div>

    </div>


    <h2>Application Health</h2>

    <div class="card">
        <div class="row">
            <span class="label">API Health Check</span>
            <span class="healthy">
                <span class="dot"></span>Healthy
            </span>
        </div>
    </div>


    <footer>
        DevOps Internship Project • Training Environment
    </footer>

</div>

</body>
</html>
"""


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        service="internship-app",
        timestamp=datetime.now().isoformat()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
