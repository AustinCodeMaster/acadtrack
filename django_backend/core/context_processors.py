from core.models import Subject, UserAccount

ACTIVE_SUBJECT_SESSION_KEY = 'active_subject_id'


def subject_context(request):
    user = getattr(request, 'user', None)
    if not user or not user.is_authenticated:
        return {
            'active_subject': None,
            'teacher_subjects': Subject.objects.none(),
            'show_subject_switch': False,
        }

    account = UserAccount.objects.filter(user=user).first()
    if not account or account.role != UserAccount.ROLE_TEACHER:
        return {
            'active_subject': None,
            'teacher_subjects': Subject.objects.none(),
            'show_subject_switch': False,
        }

    teacher_subjects = account.subjects.all()
    active_subject = teacher_subjects.filter(pk=request.session.get(ACTIVE_SUBJECT_SESSION_KEY)).first()
    return {
        'active_subject': active_subject,
        'teacher_subjects': teacher_subjects,
        'show_subject_switch': teacher_subjects.exists(),
    }
