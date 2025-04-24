# import pyautogui
# import time

# def send_message(message):
#     pyautogui.typewrite(message)
#     pyautogui.press('enter')

# with open('text.txt', 'r') as file:
#     lines = file.readlines()

# time.sleep(2)

# for line in lines:
#     send_message(line.strip())
#     # time.sleep(2)

# '''
# Write me exactly 100 lines with every line on next line on the topic 
# '''



# import pyautogui
# import time

# import pyautogui
# import time

# def send_message(message):
#     pyautogui.typewrite(message)
#     pyautogui.press('enter')

# # Delay to allow time for the user to switch to the target application
# time.sleep(2)

# # Function to determine the ordinal suffix
# def get_ordinal_suffix(number):
#     if 10 <= number % 100 <= 20:  # Special case for teens
#         return "th"
#     last_digit = number % 10
#     if last_digit == 1:
#         return "st"
#     elif last_digit == 2:
#         return "nd"
#     elif last_digit == 3:
#         return "rd"
#     else:
#         return "th"

# # Loop to send the message 1000 times
# for i in range(408, 441):
#     suffix = get_ordinal_suffix(i)
#     send_message(f"{i}. It is the {i}{suffix} message I am sending you.")

import pyautogui
import time

def send_message(message):
    time.sleep(2)
    for i in message:
        pyautogui.typewrite(i)
        # time.sleep(0.00000000001)
    pyautogui.press('enter')


message = """
Environmental pollution is one of the most pressing challenges facing humanity today. It refers to the contamination of natural resources such as air, water, and soil by harmful substances, primarily due to human activities. Pollution has far-reaching consequences for ecosystems, human health, and the planet's overall stability. Despite global awareness, the problem continues to grow, threatening the balance of life on Earth.

Air pollution is perhaps the most visible and immediate form of environmental degradation. It results from the release of harmful gases and particles into the atmosphere through industrial emissions, vehicle exhaust, and deforestation. Polluted air causes respiratory and cardiovascular diseases, including asthma, lung cancer, and heart failure. Moreover, it reduces the quality of life and contributes significantly to global warming, as greenhouse gases like carbon dioxide trap heat in the atmosphere. This exacerbates climate change, leading to rising temperatures, melting ice caps, and unpredictable weather patterns.

Water pollution, another major issue, arises from industrial effluents, agricultural runoff, and improper waste disposal. Rivers, lakes, and oceans are contaminated with chemicals, plastics, and sewage, harming aquatic ecosystems and reducing water quality. Polluted water poses serious health risks to humans, causing diseases such as cholera, dysentery, and mercury poisoning. Moreover, the destruction of marine habitats, including coral reefs, disrupts biodiversity and endangers countless species, some of which are vital to human food chains.

Soil pollution, often underestimated, is equally damaging. The excessive use of chemical fertilizers and pesticides in agriculture depletes soil nutrients and contaminates the land. Industrial and household waste further exacerbates this problem by introducing toxins into the soil. Polluted soil reduces agricultural productivity, threatening food security and the livelihoods of farmers. Additionally, toxic chemicals in the soil can enter the food chain, harming human and animal health.

The consequences of pollution extend beyond individual ecosystems, affecting biodiversity on a global scale. As natural habitats are polluted or destroyed, numerous plant and animal species face extinction. This loss of biodiversity weakens ecosystems, making them less resilient to environmental changes and reducing their ability to provide essential services such as carbon storage, water purification, and pollination. These disruptions directly impact human well-being and survival.

Climate change is intrinsically linked to environmental pollution. The burning of fossil fuels and deforestation release greenhouse gases that accelerate global warming. Rising temperatures result in more frequent and severe natural disasters, such as hurricanes, floods, and droughts. These events not only devastate communities but also strain global economies by causing damage to infrastructure and disrupting food and water supplies.

The human toll of pollution is immense, affecting millions of lives worldwide. In urban areas, air pollution causes a rise in chronic illnesses, particularly among children and the elderly. Waterborne diseases in developing countries lead to high mortality rates, especially in regions with limited access to clean drinking water. Soil contamination reduces food quality, leading to long-term health issues. These impacts disproportionately affect marginalized communities, deepening social and economic inequalities.

Economic losses due to pollution are staggering. Healthcare costs related to pollution-induced diseases are rising, placing a heavy burden on individuals and governments. The degradation of ecosystems and the loss of biodiversity disrupt industries such as agriculture, fishing, and tourism, resulting in significant financial losses. Furthermore, the cost of cleaning up polluted environments is immense, diverting resources that could be used for development.

Efforts to combat pollution are underway but remain insufficient. Governments and organizations worldwide are implementing policies to reduce emissions, promote renewable energy, and regulate waste management. However, these measures need to be intensified and supported by individual actions, such as reducing waste, conserving energy, and adopting sustainable lifestyles. Education and awareness campaigns play a crucial role in motivating people to take responsibility for the environment.

In conclusion, environmental pollution is a multifaceted problem that affects every aspect of life on Earth. Its adverse effects on air, water, soil, biodiversity, and human health underscore the urgent need for collective action. By embracing sustainable practices, investing in green technologies, and enforcing stricter environmental regulations, we can mitigate the effects of pollution and work towards a healthier planet. The responsibility lies with everyone to protect the environment for future generations."""

a = time.time()

send_message(message)
print(len(message))

print(time.time() - a)


