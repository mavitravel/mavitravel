from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        amount = request.form.get("amount")
        currency = request.form.get("currency")
        if amount and currency:
            try:
                amount = float(amount)
                # تبدیل ساده بدون API
                if currency == "تومان به دلار":
                    result = f"{amount / 42000:.2f} دلار"  # مثال نرخ ثابت
                elif currency == "دلار به تومان":
                    result = f"{amount * 42000:.2f} تومان"
                elif currency == "تومان به لیر":
                    result = f"{amount / 3.5:.2f} لیر"
                elif currency == "لیر به تومان":
                    result = f"{amount * 3.5:.2f} تومان"
            except:
                result = "مقدار نامعتبر است"
    return render_template("home.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
