<?php
error_reporting(0);

$calc = $_GET['calc'] ?? '';

$blacklist = '/(system|exec|shell|passthru|cat|flag|`|\$|\||&|;)/i';

if ($calc) {
    if (preg_match($blacklist, $calc)) {
        die("Invalid calculation!");
    }

    eval('$result = ' . $calc . ';');
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PML Bank | Loan Calculator</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            margin: 0;
            font-family: "Segoe UI", Tahoma, Arial, sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: #ffffff;
            width: 420px;
            border-radius: 14px;
            padding: 30px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.35);
        }
        .header {
            text-align: center;
            margin-bottom: 25px;
        }
        .header h1 {
            margin: 0;
            font-size: 22px;
            color: #203a43;
        }
        .header p {
            margin-top: 6px;
            font-size: 14px;
            color: #777;
        }
        label {
            font-size: 13px;
            color: #555;
            display: block;
            margin-bottom: 6px;
        }
        input[type="text"] {
            width: 100%;
            padding: 12px 14px;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 15px;
            margin-bottom: 15px;
            transition: border-color .2s;
        }
        input[type="text"]:focus {
            outline: none;
            border-color: #203a43;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #203a43;
            color: #fff;
            border: none;
            border-radius: 8px;
            font-size: 15px;
            cursor: pointer;
            transition: background .2s;
        }
        button:hover {
            background: #162b33;
        }
        .result {
            margin-top: 20px;
            padding: 14px;
            background: #f3f7fa;
            border-left: 4px solid #203a43;
            border-radius: 6px;
            font-family: Consolas, monospace;
            font-size: 14px;
            color: #333;
            word-break: break-all;
        }
        .footer {
            margin-top: 22px;
            font-size: 11px;
            color: #999;
            text-align: center;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>PML Bank</h1>
        <p>Loan Calculator</p>
    </div>

    <form method="GET">
        <label for="calc">Loan Calculation Formula</label>
        <input
            type="text"
            id="calc"
            name="calc"
            placeholder="Example: (100000 * 5) / 12"
            autocomplete="off"
        >
        <button type="submit">Calculate</button>
    </form>

    <?php if (isset($result)): ?>
        <div class="result">
            Result: <?= htmlspecialchars($result) ?>
        </div>
    <?php endif; ?>

    <div class="footer">
        © PML Bank. Secure financial services.
    </div>
</div>

</body>
</html>
