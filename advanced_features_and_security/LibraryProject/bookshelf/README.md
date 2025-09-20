# Permissions & Groups Setup

## Custom Permissions
The `Book` model defines the following permissions:
- `can_view` – Allows viewing books.
- `can_create` – Allows creating books.
- `can_edit` – Allows editing books.
- `can_delete` – Allows deleting books.

## Groups
We have defined 3 groups:
- **Viewers** – Only `can_view`
- **Editors** – `can_view`, `can_create`, `can_edit`
- **Admins** – All permissions

## Usage
- Permissions are enforced in views using the `@permission_required` decorator.
- Groups can be managed in Django Admin or via the `setup_groups` management command.
