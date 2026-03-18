from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Deadline
from app.services.scheduler import generate_schedule

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/schedule/regenerate', methods=['POST'])
def regenerate_schedule():
    data = request.get_json() or {}
    deadline_id = data.get('deadline_id')

    if deadline_id:
        deadline = db.session.get(Deadline, deadline_id)
        if not deadline:
            return jsonify({'error': 'Deadline not found'}), 404
        deadlines = [deadline]
    else:
        deadlines = db.session.query(Deadline).filter_by(is_active=True).all()
        if not deadlines:
            return jsonify({'error': 'No active deadline'}), 404

    for deadline in deadlines:
        for item in list(deadline.schedule_items):
            db.session.delete(item)
        db.session.flush()
        generate_schedule(deadline)

    db.session.commit()
    return jsonify({'status': 'ok'})
