from app import db
from app.models import Api

#************************
#=> UPDATE manager
class UpdateManager(object):
    def __init__(self):
        pass

    @staticmethod
    def update_req(request):
        try:
            req_update = request.form.get('req_update')
            update = update.query.filter_by(req_update=req_update).first()
            
            if not update:
                return dict(
                    status='FAIL',
                    message='No such update',
                    request_args=request.form,
                    error='No such update')

            org_name = request.form.get('org_name')
            update.org_name = org_name
            db.session.commit()
            return dict(status='OK', message='update updated successfully.', error=None)

        except Exception as e:
            return dict(
                status='FAIL',
                message='Could not updated this update. An unexpected error has occured.',
                request_args=request.form,
                error=str(e))