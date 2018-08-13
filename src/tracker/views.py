import json
from datetime import datetime, timedelta

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from geopy.distance import distance

from tracker.models import Route


@require_http_methods(["POST"])
def route(request):
    route = Route.objects.create()
    return JsonResponse({
        'route_id': route.id
    }, status=201)


@require_http_methods(["DELETE"])
def delete_route(request, route_id):
    try:
        route = Route.objects.get(id=route_id).delete()
    except Route.DoesNotExist as err:
        return JsonResponse({'error': f'No route with id: {route_id}'}, status=404)
    return JsonResponse({'succes': f'Route {route_id} deleted'}, status=204)


@require_http_methods(["POST"])
def way_point(request, route_id):
    try:
        route = Route.objects.get(id=route_id)
    except Route.DoesNotExist as err:
        return JsonResponse({'error': f'No route with id: {route_id}'}, status=404)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError as err:
        return JsonResponse({'error': 'Invalid json format'}, status=400)
    lat = data.get('lat')
    lon = data.get('lon')
    if isinstance(lat, float) and isinstance(lon, float):
        point = (lat, lon)
        if route.coordinates:
            last_distance = distance(route.coordinates[-1], point)
            route.length += last_distance.kilometers
        route.coordinates.append(point)
        route.save()
        return JsonResponse({
            'route_id': route_id,
            'way_points': route.coordinates,
            'length': route.length
        }, status=201)
    return JsonResponse({
        'error': 'Invalid coordinates type!'
    }, status=400)


@require_http_methods(["GET"])
def length(request, route_id):
    try:
        route = Route.objects.get(id=route_id)
    except Route.DoesNotExist as err:
        return JsonResponse({'error': f'No route with id: {route_id}'}, status=404)

    return JsonResponse({
        'route_id': route.id,
        'km': route.length
    })


@require_http_methods(["GET"])
def longest_route(request, date):
    date = datetime.strptime(date, "%Y-%m-%d")
    next_day = date + timedelta(days=1)
    routes = Route.objects.filter(
        created_at__gte=date,
        created_at__lt=next_day
    ).order_by('-length')
    if routes:
        longest_route = routes[0]
        return JsonResponse({
            'longest_route': {
                'route_id': longest_route.id,
                'km': longest_route.length,
                'way_points': longest_route.coordinates
            }
        })

    return JsonResponse({'error': f'No routes found for {date}'}, status=404)
