# Repository Guidelines — Resources by xdecaro

Resources is a separate Joomla product in the xdecaro ecosystem.

## Domain boundary

Resources owns reusable allocatable resource definitions and capacity/availability-oriented metadata. Bookings owns reservations and calendars; Inventory owns stock and physical item movements. A resource may reference an Inventory item through a public contract, never through private-table coupling.

Core by xdecaro provides only shared infrastructure: Web Asset Manager assets, design tokens, compatibility helpers, diagnostics and public cross-product reference contracts. Do not move Resources-specific business rules into Core.

Dependency direction is `Resources -> Core`, never `Core -> Resources`. Never read or write another product's private tables.

## Joomla/security

Use modern Joomla APIs, server-side ACL, CSRF for state-changing operations, validated input, escaped output, bound database queries and `#__` table prefixes. Availability metadata in Resources must not become a hidden booking engine; reservation state belongs to Bookings.

## Releases

Version 0.2.0 establishes the first technical baseline. Keep stable IDs `com_xdecaroresources` and `pkg_xdecaroresources`. Normal updates must preserve data and configuration.
