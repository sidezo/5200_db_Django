from django.shortcuts import render
from .models import Orders, Customers, Parts, Odetails
# Import any other necessary models

def order_details(request, order_id):
    # Fetch the order based on the provided order_id
    try:
        order = Orders.objects.get(ono=order_id)
    except Orders.DoesNotExist:
        return render(request, 'order_details.html', {'order_id': order_id})

    # Fetch related data
    customer = Customers.objects.get(cno=order.cno)
    order_details = Odetails.objects.filter(ono=order_id)

    # Prepare data for rendering
    details = []
    total = 0
    for detail in order_details:
        part = detail.pno  # Access the related Parts object directly
        subtotal = part.prices * detail.qty
        total += subtotal
        details.append({
            'part_no': part.pno,    # part.pno is the primary key of the Parts object
            'part_name': part.pname,
            'quantity': detail.qty,
            'price': part.prices,
            'subtotal': subtotal,
    })

    context = {
        'customer': customer,
        'order': order,
        'details': details,
        'total': total
    }

    return render(request, 'order_details.html', context)
