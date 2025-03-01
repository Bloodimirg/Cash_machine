import os
import qrcode
import pdfkit

from django.http import FileResponse
from django.template.loader import render_to_string

from cash_machine.models import Item
from django.conf import settings


def get_item_details(item_ids):
    # Получаем товары по их id
    items = Item.objects.filter(id__in=item_ids)
    if not items:
        return None, "Товары не найдены."

    total = 0
    item_details = []

    for item in items:
        quantity = 1  # количество товаров
        total_price = item.price * quantity
        item_details.append(
            {"title": item.title, "quantity": quantity, "total_price": total_price}
        )
        total += total_price

    return item_details, total


def generate_pdf(item_details, total, time, receipt_id):
    # Генерация HTML из шаблона
    html_content = render_to_string(
        "cash_machine/receipt_template.html",
        {"items": item_details, "total": total, "time": time, "receipt_id": receipt_id},
    )

    # Генерация PDF
    pdf_filename = f"receipt_{receipt_id}.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
    pdfkit.from_string(html_content, pdf_path)

    return pdf_filename


def generate_qr(pdf_filename):
    pdf_url = f"{settings.SITE_URL}/media/{pdf_filename}"

    # Генерация QR-кода со ссылкой на PDF
    qr = qrcode.make(pdf_url)

    # Сохранение QR-кода в папку media
    qr_filename = pdf_filename.replace(".pdf", ".png")
    qr_path = os.path.join(settings.MEDIA_ROOT, qr_filename)

    qr.save(qr_path)

    return qr_filename


def serve_pdf(request, filename):
    # Формирование пути к файлу
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    # проверка существует ли файл
    if os.path.exists(file_path):
        return FileResponse(open(file_path, "rb"), content_type="application/pdf")
    else:
        from django.http import Http404

        raise Http404("PDF файл не найден.")
