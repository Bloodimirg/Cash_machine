from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from django.conf import settings
from .utils import get_item_details, generate_pdf, generate_qr


class CashMachineAPIView(APIView):
    """Создание чека"""

    def post(self, request, *args, **kwargs):
        # Получаем список товаров по их ID
        item_ids = request.data.get("items", [])

        # получение информации о товарах
        item_details, total = get_item_details(item_ids)

        # Если товары не найдены, возвращаем ошибку
        if item_details is None:
            return Response({"detail": total}, status=status.HTTP_404_NOT_FOUND)

        # Генерация времени чека
        time = now().strftime("%d.%m.%Y %H:%M")

        # Генерация уникального ID для чека
        receipt_id = now().strftime("%Y%m%d%H%M%S")

        # Генерация PDF для чека
        pdf_filename = generate_pdf(item_details, total, time, receipt_id)

        # Генерация QR-кода со ссылкой на PDF
        qr_filename = generate_qr(pdf_filename)

        # Формируем URL для скачивания PDF и QR-кода
        pdf_url = f"{settings.SITE_URL}/media/{pdf_filename}"
        qr_code_url = f"{settings.SITE_URL}/media/{qr_filename}"

        # Возвращаем ссылку на QR-код
        return Response(
            {"pdf_url": pdf_url, "qr_code_url": qr_code_url}, status=status.HTTP_200_OK
        )
