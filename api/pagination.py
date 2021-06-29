from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginacaoCustomizada(PageNumberPagination):
    page_size = 3   # Quantidades de itens por página
    page_size_query_param = "tamanho_pagina"    # Altera quantidade de itens da página
    max_page_size = 10  # Limita a quantidade itens

    def get_paginated_response(self, data):
        return Response({
            'total_itens': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'results': data
        })