#diet_plan 2
import pandas as pd
from datetime import datetime
today=datetime.now()
Day=datetime.now()
date=today.strftime("%d/%m/%Y")
today_day=Day.strftime("%A")

print()


print(date,today_day)

print("\n\nDIET PLAN 🏋️   🏃  🧘‍♂️")

print("\n")

login=input("login:")
password=input("enter password:")


if login == "Admin" and password =="Admin@1234":
    print("login successfully")
    
else:
    print("INVALID LOGIN ")
    exit()


print()
age=int(input("enter age :"))
if age <18:
    exit()
weight=int(input("enter weight (Kg) :"))
height=int(input("enter height (cm) :"))
height = height/100
BMI = (weight/(height*height))
print("="*50)
print("BMI REPORT")
print("="*50)

print("\n your bmi(BODY MASS INDEX):",round(BMI,2))
print("="*50)


print("\n\n Here are BMI Categories : ")
print("="*50)
bmi_data = {
    "BMI":["Less than 18.5","18.5 to 24.9","25  to 29.9","30 or more"],
    "Category":["Underweight","Normal Weight","Overweight","Obesity"]
}

df=pd.DataFrame(bmi_data)
print()

print(df)
print("="*50)

print("\nsuggestions:")
if BMI <=18.5 :
    print("\nyou are Underweight")
    print("\nI suggest you diet_plan:Weight gain")
elif 18.5  <=BMI<= 24.5:
    print("\nyou are Normal Weight")
    print("\nI suggest you diet_plan :Healthy maintenance")
elif 25 <=BMI<= 29.9:
    print("\nyou are Overweight")
    print("\nI suggest you diet_plan :weight_loss")
else:
    print("\n you are Obese")
    print("\nI suggest you diet_plan :weight_loss ")


print()
print("choose:")
print("\n1.weight_Loss")
print("\n2. Gain")

choose_goal =["weight_Loss","Gain"]
goal=input("enter choose goal_diet_plan:")

Weight_Loss=["vegetarian","vegan","non-vegetarian"]
gain=["vegetarian","vegan","non-vegetarian"]

if goal in choose_goal :
    print("\nTo help me tailor this diet exactly to your lifestyle, could you tell me:")
    print("\nHere some ques :")
    print("\nDo you have any dietary preferences (e.g., vegetarian/vegan/non-vegetarian)?")
    diet_types = ["vegetarian", "vegan", "non-vegetarian"]
    diet_type=input('\ntype message :').strip().lower()
    if diet_type not in diet_type:
        raise Exception("Invalid choice,Please enter valid options(vegetarian/vegan/non-vegetarian))")

if goal not in choose_goal:
    raise Exception("Invalid choice,Please enter valid options(weight_Loss","Gain))")
      
print()
print("="*50)
print("Diet Plan")
print("="*50)
if goal == "weight_Loss":
    if diet_type =="vegetarian":
       
        print("How to Build Your Meals 🥦 🍎")
        data= {
           "Vegetables (50% of the plate)": "Non-starchy options (spinach, broccoli, carrots, cucumbers). They are very low in calories, so you can eat large portions.",
            "Plant Protein (25% of the plate)":" Protein is vital to keep your muscles strong while you lose fat. Try tofu, lentils, chickpeas, black beans, or 100g of paneer",
            "Complex Carbs (25% of the plate)": "Swap refined carbs for whole grains (oats, brown rice, quinoa, whole-wheat roti). They give you long-lasting energy.",
           "Healthy Fats": "Fats (nuts, seeds, olive oil, avocado) are healthy but contain 9 calories per gram (compared to 4 calories for proteins/carbs). Watch your portions",

           "Breakfast": "1 bowl of oats or 1 vegetable poha cooked with minimal oil + 1 glass of skimmed milk.",
           "Lunch": "2 whole-wheat rotis + 1 cup lentil dal + large mixed salad.",
           "Snack": "Roasted chickpeas or 1 cup of curd.",
          "Dinner":" Tofu or paneer curry + half(1/2) cup brown rice + steamed vegetables"
        }
        for i,j in data.items():
            print(f"\n{i}:  {j}")
    elif diet_type == "vegan":
               

        print("How to Build Your Meals 🥦 🍎")
        data1={
            "Breakfast": "1/2 cup quick oats cooked in water with 1 tbsp peanut butter, 1 tbsp chia seeds, and 1/2 cup berries.",
            "Lunch": "Tofu scramble made with 1/2 block extra-firm tofu, spinach, mushrooms, and 1/2 cup cooked quinoa.",
            "Dinner": "Chickpea and cauliflower curry (1 cup chickpeas) with 1/2 cup cooked brown rice.",
            "Snack":" 1 apple with 1 tbsp almond butte"
        }
        for i,j in data1.items():
            print(f"{i}:{j}")
    elif diet_type == "non-vegetarian":
        print("\nHow to Build Your Meals 🍗 🥩")
        data3={
            "1.Early Morning (Metabolism Boosters)":
            "Warm water with lemon juiceWarm,"
            " water with cumin seeds (jeera),"
            "Plain warm water",

            "2.Breakfast (High Protein)":"2 boiled eggs with 1 slice of whole-wheat toast,"
            "Egg-white omelette cooked with onions and tomatoes,"
            "1 bowl of oatmeal with skimmed milk and fresh berries",

            "3.Lunch (Lean Protein + Complex Carbs)":"Grilled chicken breast paired with a large mixed salad,"
            "Baked fish served with a small bowl of brown rice,"
            "Shredded chicken salad mixed with plain yogurt and diced vegetables",

            "4.Evening Snack (Satiety Helpers)":"1 cup of green tea accompanied by a handful of almonds,"
            "1 cup of plain unsweetened yogurt,"
            "1 small bowl of dry-roasted chickpeas (chana)",

            "5.Dinner (Light & Low Carb)":"1 bowl of clear vegetable soup with 1 boiled egg,"
            "Chicken or fish stew served with sautéed spinach,"
            "1 bowl of yellow lentil soup (dal) with 1 whole-wheat roti"
        }
        for i,j in data3.items():
            print(f"{i}:{j}")

elif goal == "Gain":
    if  diet_type == "vegetarian" :
        print("\nHow to Build Your Meals 🥬 🥗")
        print("\nWomen: 2,200 to 2,500 calories per day.,\nMen: 2,600 to 3,000 calories per day")
        print("\nTop High-Calorie Vegetarian Foods")
        data4={
            "Breakfast (approx. 750 calories)Oatmeal": "1 cup rolled oats cooked in 1.5 cups whole milk or soy milk.",
            "Toppings": "2 tablespoons peanut butter, 1 chopped banana, 2 tablespoons hemp seeds, and 1 tablespoon honey",
            "Mid-Morning Snack (approx. 400 calories)Nut & Fruit Mix": "1/4 cup almonds, 1/4 cup walnuts, and 1/4 cup raisins or dried cranberries.",
            
            "Lunch (approx. 750 calories)Chickpea & Avocado Wrap": "2 large whole-wheat tortillas filled with 1 cup mashed chickpeas.",
            "Fats & Veggies":" 1/2 mashed avocado, 2 tablespoons olive oil mayonnaise, spinach, and tomato slices.Side: 1 cup of full-fat Greek yogurt (or high-protein plant yogurt).",
            
            "Afternoon Snack (approx. 400 calories)Weight Gain Smoothie": "Blend 1 cup whole milk or pea milk, 1 scoop vegetarian protein powder, 1 tablespoon almond butter, and 1 cup frozen berries",
            
            "Dinner (approx. 700 calories)Tofu Stir-Fry": "200g firm tofu cubes sautéed in 2 tablespoons of sesame oil.",
            "Grains & Veggies": "Serve over 1.5 cups of cooked brown rice or quinoa with mixed vegetables (broccoli, bell peppers, carrots).",
            "Topping": "2 tablespoons of sesame seeds or chopped cashews."

        }
        for i,j in data4.items():
            print(f"{i}:{j}")

    elif diet_type == "vegan":
        print("\nHow to Build Your Meals 🥬 🥗")
        data5={
            "Breakfast": "Oatmeal made with soy milk, 1 sliced banana, 2 tablespoons of peanut butter, and a handful of walnuts.",
            "Lunch": "Chickpea pasta mixed with crumbled tempeh and olive oil.",
            "Snack": "Apple slices with almond butter or a homemade trail mix.",
            "Dinner": "Black bean bowl with brown rice, diced avocado, and tahini dressing.",
            "Bedtime": "A plant-based protein shake blended with soy milk"
        }
        for i,j in data5.items():
            print(f"{i}:{j}")

    elif diet_type == "non-vegetarian":
        print("\nHow to Build Your Meals 🍗 🥩")
        data6={
            "Early Morning": "A glass of full-fat milk, with a small serving of almonds and walnuts.",
            "Breakfast": "Scrambled eggs, whole-wheat toast, and a banana.",
            "Mid-Morning": "A serving of fruit (such as papaya or banana) and a handful of peanuts.",
            "Lunch": "A bowl of chicken or mutton curry, a generous serving of cooked rice, and a mixed vegetable salad.",
            "Evening": "A tuna or chicken sandwich, and a glass of fresh lime water.",
            "Dinner": "A portion of baked or grilled fish or chicken breast, stir-fried vegetables, and quinoa or brown rice.",
            "Bedtime": "A glass of warm full-fat milk with a pinch of turmeric"
        }
        for i,j in data6.items():
            print(f"{i}:{j}")


print("\nAlert!")
print("\n" + "="*60)
print(" IMPORTANT DISCLAIMER")
print("="*60)
print("• This diet plan is for educational and practice purposes only.")
print("• It is a general example and may not be suitable for everyone.")
print("• Every person has different nutritional needs, allergies,")
print("  medical conditions, and fitness goals.")
print("• Please consult a qualified doctor or registered dietitian")
print("  before following any diet plan.")
print("="*60)



