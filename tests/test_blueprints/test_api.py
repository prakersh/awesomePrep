from datetime import date, timedelta
from app.models import Deadline


class TestScheduleRegenerateAPI:
    def test_regenerate_no_deadline(self, client, db):
        resp = client.post('/api/schedule/regenerate', json={})
        assert resp.status_code == 404

    def test_regenerate_schedule(self, client, db, sample_language, sample_concept):
        d = Deadline(
            language_id=sample_language.id,
            interview_date=date.today() + timedelta(days=30),
            is_active=True,
        )
        db.session.add(d)
        db.session.commit()
        resp = client.post('/api/schedule/regenerate', json={})
        assert resp.status_code == 200
        assert resp.get_json()['status'] == 'ok'

    def test_regenerate_specific_deadline(self, client, db, sample_language, sample_concept):
        d = Deadline(
            language_id=sample_language.id,
            interview_date=date.today() + timedelta(days=30),
            is_active=True,
        )
        db.session.add(d)
        db.session.commit()
        resp = client.post('/api/schedule/regenerate', json={'deadline_id': d.id})
        assert resp.status_code == 200
