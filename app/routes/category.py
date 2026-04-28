# app/routes/category.py
"""Category (custom tag) routes skeleton."""

from flask import Blueprint, render_template, request, redirect, url_for, flash

category_bp = Blueprint('category', __name__, url_prefix='/categories')

@category_bp.route('/', methods=['GET'])
def list_categories():
    """Display list of user-defined categories."""
    pass

@category_bp.route('/add', methods=['GET'])
def add_category_form():
    """Render form to create a new category."""
    pass

@category_bp.route('/add', methods=['POST'])
def add_category():
    """Process new category form and create record."""
    pass

@category_bp.route('/<int:id>/edit', methods=['GET'])
def edit_category_form(id):
    """Render form to edit an existing category."""
    pass

@category_bp.route('/<int:id>/edit', methods=['POST'])
def edit_category(id):
    """Process edit form and update category."""
    pass

@category_bp.route('/<int:id>/delete', methods=['POST'])
def delete_category(id):
    """Delete specified category and redirect to list."""
    pass
