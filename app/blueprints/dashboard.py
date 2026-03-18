from flask import Blueprint, render_template
from datetime import date
from app.extensions import db
from app.models import Language, Question, Deadline, ScheduleItem, Concept

bp = Blueprint('dashboard', __name__)


@bp.route('/')
def index():
    total_questions = db.session.query(Question).count()

    # All active deadlines sorted by date
    deadlines = (
        db.session.query(Deadline)
        .filter_by(is_active=True)
        .order_by(Deadline.interview_date)
        .all()
    )

    deadline_data = []
    for d in deadlines:
        days_remaining = (d.interview_date - date.today()).days
        deadline_data.append({'deadline': d, 'days_remaining': days_remaining})

    # Languages with question IDs for client-side progress hydration
    languages = db.session.query(Language).filter_by(is_active=True).order_by(Language.display_order).all()

    language_stats = []
    for lang in languages:
        qids = []
        concepts_data = []
        for c in lang.concepts:
            c_qids = [q.id for q in c.questions]
            qids.extend(c_qids)
            concepts_data.append({
                'concept': c,
                'qids': c_qids,
                'total': len(c_qids),
            })
        language_stats.append({
            'language': lang,
            'total': len(qids),
            'qids': qids,
            'concept_count': len(lang.concepts),
            'concepts': concepts_data,
        })

    # Per-difficulty stats with question IDs
    difficulty_stats = []
    for diff in ['beginner', 'intermediate', 'advanced']:
        concepts = db.session.query(Concept).filter_by(difficulty=diff).all()
        qids = []
        for c in concepts:
            qids.extend(q.id for q in c.questions)
        difficulty_stats.append({
            'difficulty': diff,
            'total': len(qids),
            'qids': qids,
        })

    # Question metadata for recent-viewed hydration (JS needs title + URL info)
    all_questions = {}
    for ls in language_stats:
        for cd in ls['concepts']:
            for q in cd['concept'].questions:
                all_questions[q.id] = {
                    'title': q.title,
                    'url': f"/study/{ls['language'].slug}/{cd['concept'].slug}?q={q.id}",
                }

    return render_template(
        'dashboard/index.html',
        total_questions=total_questions,
        deadline_data=deadline_data,
        language_stats=language_stats,
        difficulty_stats=difficulty_stats,
        all_questions=all_questions,
    )
