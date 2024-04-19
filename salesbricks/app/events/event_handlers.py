# app/events/event_handlers.py
from .event_types import ORDER_CLOSED_WON, ORDER_CLOSED_LOST, ORDER_CLOSED_WON_REVENUE

""" Event handlers for processing order events. """
def handle_order_closed_won(order_id: int):
    print(f"Processing ORDER_CLOSED_WON for order {order_id}")
    # Process the event, e.g., update order status in the database

def handle_order_closed_lost(order_id: int):
    print(f"Processing ORDER_CLOSED_LOST for order {order_id}")
    # Additional processing

def handle_order_closed_won_revenue(order_id: int, revenue: float):
    print(f"Processing ORDER_CLOSED_WON_REVENUE for order {order_id} with revenue {revenue}")
    # Update revenue tracking systems

# Map event types to their handlers for dynamic dispatch
event_dispatcher = {
    ORDER_CLOSED_WON: handle_order_closed_won,
    ORDER_CLOSED_LOST: handle_order_closed_lost,
    ORDER_CLOSED_WON_REVENUE: handle_order_closed_won_revenue,
}

def dispatch_event(event_type: str, *args, **kwargs):
    """Dispatch event to the appropriate handler."""
    if event_type in event_dispatcher:
        event_dispatcher[event_type](*args, **kwargs)
    else:
        raise ValueError(f"Unhandled event type: {event_type}")
