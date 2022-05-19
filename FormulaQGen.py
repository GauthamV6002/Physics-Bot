import random
import re

QUESTION_GENERATOR_LIST = {
  "kinematics": [],
  "circular motion": [],
  "work/energy": [],
  "harmonic motion": []
}

class QuestionGenerator:
  def __init__(self, variables, lhs, category): #lhs must give the final value in variables
    global QUESTION_GENERATOR_LIST
    if category in QUESTION_GENERATOR_LIST:
      QUESTION_GENERATOR_LIST[category].append(self)
    else:
      QUESTION_GENERATOR_LIST[category] = [self]
    self.variables = variables
    self.lhs = lhs

  def safe_eval(self, s):
    numeric_s = re.sub('[^a-zA-Z0-9 \n\.]', '', s).replace(" ", "").replace(".", "")
    if numeric_s.isnumeric():
      return eval(s)
    else:
      raise Exception(f"Eval Operation unsafe! Check inputted formulas.\nNumeric Expression {numeric_s} was not numeric!")

  def question_values(self):
    filledVariables = {}
    filled_lhs = self.lhs
    
    for variable in self.variables[:-1]:
      filledVariables[variable] = round(random.random() * random.randint(1, 50), 2)
      filled_lhs = filled_lhs.replace(variable, str(filledVariables[variable]))

    filledVariables[self.variables[-1]] = round(self.safe_eval(filled_lhs), 5)
    return filledVariables
    

#Formulas:
  
kinematics_vf = QuestionGenerator(["vi", "t", "a", "vf"], "vi + (a*t)", "kinematics")
kinematics_d = QuestionGenerator(["vi", "vf", "t", "d"], "((vf + vi) * 0.5) * t", "kinematics")
kinematics_d2 = QuestionGenerator(["vi", "t", "a", "d"], "(vi * t) + (0.5 * a * t*t)", "kinematics")
kinematics_vsquared = QuestionGenerator(["vi", "a", "d", "vf"], "((vi*vi) + (2 * a *d)) ** (0.5)", "kinematics") #math.sqrt will NOT work, ** (1/2) should be used instead

hookes_law = QuestionGenerator(["k", "x", "Fs"], "-1 * k * x", "harmonic motion")
elastic_potential_energy = QuestionGenerator(["k", "x", "Epe"], "0.5 * k * (x*x)", "harmonic motion")
spring_period = QuestionGenerator(["m", "k", "T"], "2 * 3.14159 * ((m / k) ** (0.5))", "harmonic motion")
pendulum_period = QuestionGenerator(["length", "T"], "2 * 3.14159 * ((l / 9.81) ** (0.5))", "harmonic motion")

grav_pot_energy = QuestionGenerator(["m", "h", "Epg"], "m * 9.81 * h", "work/energy")
kinetic_energy = QuestionGenerator(["m", "v", "Ek"], "0.5 * m * v*v", "work/energy")
work = QuestionGenerator(["F", "d", "W"], "F * d", "work/energy")

period_to_freq = QuestionGenerator(["f", "T"], "1 / f", "circular motion")
tangential_velocity = QuestionGenerator(["r", "T", "v-centripetal"], "2 * 3.14159 * (1 / T)", "circular motion")
centripetal_acceleration_from_velocity = QuestionGenerator(["v", "r", "a-centripetal"], "v*v / r", "circular motion")
centripetal_acceleration_from_period = QuestionGenerator(["r", "T", "a-centripetal"], "(4 * 3.14159 * 3.14159 * r) / (T * T)", "circular motion")