from django.test import TestCase, Client
from django.urls import reverse

class AdminViewTests(TestCase):
    def test_admin_login_page_loads(self):
        """
        Test that the admin login page loads correctly.
        It might return 200 if already somehow authenticated by default test client setup,
        or 302 if it redirects to a login page.
        """
        client = Client()
        # Try fetching the admin login URL.
        # If LOGIN_URL is customized, this might need adjustment,
        # but /admin/login/ is common, or /admin/ will redirect to it.
        try:
            admin_url = reverse('admin:index')
        except Exception:
            # Fallback if 'admin:index' is not found (e.g. admin not fully set up for URL reversing)
            admin_url = '/admin/'

        response = client.get(admin_url)
        self.assertIn(
            response.status_code,
            [200, 302],
            f"Admin page ({admin_url}) returned {response.status_code}, expected 200 or 302."
        )

class CeleryTaskTests(TestCase):
    def test_add_task_importable_and_callable(self):
        """
        Test that the sample 'add' task can be imported and is callable.
        """
        try:
            from .tasks import add
            self.assertTrue(callable(add), "Add task 'add' should be callable.")
        except ImportError:
            self.fail("Could not import task 'add' from ebdjango.tasks.")
        except Exception as e:
            self.fail(f"An unexpected error occurred during task import/check: {e}")

    def test_add_task_basic_execution(self):
        """
        A very basic test of the add task's execution logic.
        Note: This runs the task synchronously in the test process, not via a Celery worker.
        """
        try:
            from .tasks import add
            result = add.delay(3, 5) # Using .delay() to simulate Celery call style
            # For testing purposes with CELERY_TASK_ALWAYS_EAGER=True (often set for tests),
            # .delay() might execute synchronously and return an EagerResult.
            # If not eager, this would return an AsyncResult.
            # We'll check if the result has a 'get' method to fetch the actual return value.
            if hasattr(result, 'get'):
                 # Timeout for safety, though eager tasks should be immediate.
                self.assertEqual(result.get(timeout=10), 8, "Task 'add(3, 5)' should return 8.")
            else:
                # Fallback for when task isn't eager and we just have an AsyncResult
                # This part of the test would be more complex in a real scenario
                # requiring worker setup or mocking. For now, we just check it didn't fail.
                self.assertIsNotNone(result.id, "Task 'add' should return an AsyncResult with an ID.")

        except ImportError:
            self.fail("Could not import task 'add' from ebdjango.tasks.")
        except Exception as e:
            self.fail(f"An unexpected error occurred during task execution test: {e}")
