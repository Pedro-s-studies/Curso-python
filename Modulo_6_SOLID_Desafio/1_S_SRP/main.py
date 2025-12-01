from src.connect import ApiClient
from src.task_service import TaskService
from src.notification_service import NotificationService
from src.report_service import ReportService

api = ApiClient()
tasks = TaskService()
notify = NotificationService()
reports = ReportService()

api.connect()
tasks.create_task()
notify.send_notification()
reports.generate_report()
