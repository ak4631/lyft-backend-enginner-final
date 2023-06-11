import unittest

from engine.sternman_engine import StermanEngine

class TestStermanEngine(unittest):
    def test_needs_service_true(self):
        warning_light_is_on=True
        engine=StermanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on=False 
        engine=StermanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    
