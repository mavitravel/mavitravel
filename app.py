from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            # گرفتن مقدار از فرم
            amount_str = request.form.get("amount", "").strip()
            currency = request.form.get("currency", "").strip()

            if amount_str == "" or currency == "":
                result = "لطفاً همه فیلدها را پر کنید."
            else:
                amount = float(amount_str)

                # تبدیل ساده بدون API
                if currency == "تومان به دلار":
                    result = f"{amount / 42000:.2f} دلار"
                elif currency == "دلار به تومان":
                    result = f"{amount * 42000:.2f} تومان"
                elif currency == "تومان به لیر":
                    result = f"{amount / 33:.2f} لیر"
                elif currency == "لیر به تومان":
                    result = f"{amount * 3100:.2f} تومان"
                else:
                    result = "ارز نامعتبر است"
        except ValueError:
            result = "مقدار وارد شده عدد نیست."
        except Exception as e:
            result = f"خطا: {e}"

    return render_template("home.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
