from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from users.models import *
from workout.models import *
from django.core.exceptions import ObjectDoesNotExist
from workout.utils import *
from unittest.mock import patch, Mock
import pytest

class TestWorkout(StaticLiveServerTestCase):
    fixtures = ["testusers.json"]

    def mock_exercise(self, number: int = 1) -> Mock:
        name = "Test Exercise " + str(number)
        mock_exercise = Mock()
        mock_exercise.name = name
        return mock_exercise
    
    def mock_workout(self) -> Mock:
        name = "Test workout"
        mock_workout = Mock()
        mock_workout.name = name
        return mock_workout

    def test_save_exercise(self) -> None:
        mock_exercise = self.mock_exercise()
        with patch("workout.utils.Exercise", return_value=mock_exercise):
            save_exercise(mock_exercise.name)
            assert mock_exercise.name == "Test Exercise 1"
            mock_exercise.save.assert_called_once()

    def test_save_workout(self) -> None:
        mock_workout = self.mock_workout()
        exercises = [self.mock_exercise(i) for i in range(3)]
        mock_workout.exercises.set.side_effect = mock_workout.exercises(exercises)

        with patch("workout.utils.Workout", return_value=mock_workout):
            save_workout(exercises)
            mock_workout.exercises.set.assert_called_with(exercises)
            mock_workout.save.assert_called_once()

    def test_save__current_workout(self) -> None:
        mock_workout_log = self.mock_workout()
        exercise_logs = [self.mock_exercise(i) for i in range(3)]
        mock_workout_log.exercises.set.side_effect = mock_workout_log.exercises(exercise_logs)

        with patch("workout.utils.Workout", return_value=mock_workout_log):
            save_workout(exercise_logs)
            mock_workout_log.exercises.set.assert_called_with(exercise_logs)
            mock_workout_log.save.assert_called_once()
        

    def test_delete_record(self) -> None:
        mock_workout = self.mock_workout()
        with patch("workout.utils.Exercise", return_value=mock_workout):
            delete_record(mock_workout)
            mock_workout.delete.assert_called_once()

            

