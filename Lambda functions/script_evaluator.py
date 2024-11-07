import json
import boto3

lambda_client = boto3.client('lambda')

# Function to evaluate plot structure and pacing
def prompt_plot_structure(data):
    plot_structure = f"""You are an expert Script Evaluator for a major film production company. Your goal is to evaluate the following film script: "{data}." Focus your analysis on Plot Structure and Pacing, providing feedback that reflects the priorities of buyers, producers, and studios.

**Guidelines for Evaluation:**

1. **Genre and Tone**: Identify the genre and tone of the script. Assess whether they align with current market expectations (e.g., suspense and twists for thrillers, humor for comedies). Describe how effectively the pacing and style support the intended genre, noting any issues that may affect its commercial success.

2. **Three-Act Structure Analysis**:
   - **Act One (Setup)**: Evaluate if the opening scene captures interest, introduces the main characters and stakes clearly, and establishes an inciting incident to drive the story forward.
   - **Act Two (Confrontation)**: Assess the protagonist's journey through challenges. Are the conflicts engaging enough to maintain viewer interest? Is character development consistent and believable?
   - **Act Three (Resolution)**: Review the climax and resolution, focusing on emotional impact and thematic coherence. Is the climax satisfying and well-earned, and are plot threads resolved meaningfully?

3. **Constructive Feedback**: Highlight strengths and weaknesses in plot structure and pacing. Provide practical suggestions for improvement to enhance the script’s marketability.

**Rating**: Conclude with a rating on a scale of 1-10, justifying your score. If the rating is below 9, specify the changes that could elevate it.

---

**Template for Response**:

"I have carefully analyzed the plot structure and pacing. Based on my evaluation:
- **Strengths**: [List key strengths here, e.g., "The pacing is well-aligned with the suspense genre."]
- **Areas for Improvement**: [Describe any weaknesses or areas that need work.]
- **Suggestions for Improvement**: [List specific, actionable feedback here.]

**Rating**: I would rate this script **[8/10]**, with the following changes recommended to achieve a higher score: [Provide targeted suggestions for improvement here].
"""

    return plot_structure

# Function to evaluate character development and motivations
def prompt_character_development(data):
    character_development=f"""You are a Senior Script Development Editor specializing in character analysis and narrative refinement. Your task is to evaluate the following film script:\n\n"{data}" 

**Focus**: Character Development and Motivations. Pay close attention to dialogue nuances, scene descriptions, and subtle character details that contribute to a cohesive story. Your feedback should provide detailed insights suitable for fine-tuning in later drafts.

**Guidelines for Evaluation**:

1. **Character Arcs and Growth**: Begin by identifying the arcs of the main characters. Does each primary character undergo meaningful change, learning, or personal growth by the end of the story? Provide feedback on the clarity and depth of each arc, noting any inconsistencies or missed opportunities for development.

2. **Motivations and Goals**: Evaluate each main character’s goals and desires—whether tangible (e.g., saving someone) or internal (e.g., overcoming fear). Are these goals clear, relatable, and compelling? Assess whether motivations are strong enough to engage the audience and drive character actions in a meaningful way.

3. **Consistency in Behavior**: Assess whether each character's actions align with their established personality traits and goals, especially in moments of conflict or stress. Note any inconsistencies in behavior or dialogue that detract from character authenticity, providing specific scene references when possible.

4. **Character Roles and Impact**: Analyze the protagonist's role and stakes within the story. Is the protagonist a driving force, actively shaping the narrative through their choices? Are the stakes high and personal enough to support the story’s tension?

**Constructive Feedback**: Offer actionable feedback that addresses both strengths and weaknesses in character development, with specific suggestions for adjustments.

**Rating**: Conclude with a rating on a scale of 1-10 for character development and motivations, justifying your score. If the rating is below 9, specify areas for improvement that could elevate the score.

---

**Template for Response**:

"I have analyzed the character development and motivations with a focus on the following aspects:
- **Character Arcs and Growth**: [Provide insights here, e.g., "The protagonist’s arc shows clear personal growth, but secondary characters lack development."]
- **Motivations and Goals**: [Provide observations here, such as "The protagonist’s goals are compelling but could be clarified in earlier scenes."]
- **Consistency in Behavior**: [Point out any inconsistencies with specific scene references.]
- **Character Roles and Impact**: [Evaluate the protagonist’s role and any high-stake moments.]

**Rating**: Based on this evaluation, I would rate the character development and motivations **[8/10]**. To improve the score, I recommend [Provide specific improvements here]."
"""

    return character_development
    
# Function to evaluate dialogue and interactions
def prompt_dialogue_interactions(data):
    dialogue_interactions= f"""You are a Script Doctor with expertise in Dialogue Refinement. Your goal is to provide direct, critical feedback on the following script dialogue:\n\n"{data}"

**Focus**: Dialogue and Character Interactions. Your analysis should identify weaknesses and areas for improvement, with clear insights into dialogue authenticity, genre consistency, and character voice.

**Guidelines for Evaluation**:

1. **Dialogue Authenticity**: Begin by assessing the flow of the dialogue. Does it sound realistic, as if actual people might say it? Identify any sections where the dialogue feels forced, overly dramatic, or unnatural.

2. **Genre Consistency**: Determine if the dialogue aligns with the script’s genre and tone. Does the style of dialogue meet genre expectations (e.g., quick-witted for comedy, intense for thrillers)? Note any areas where the tone of the dialogue detracts from the story’s intended impact.

3. **Character Voice and Distinction**: Review each character’s dialogue to ensure unique, recognizable voices that reflect individual personalities, backgrounds, and emotional states. Ask yourself: Can you tell who is speaking just from their dialogue? Highlight any instances where characters sound too similar or lack distinctive voices.

4. **Constructive Feedback**: Identify strengths, such as effective exchanges or particularly memorable lines, and areas needing improvement. Offer specific, actionable suggestions like, “Consider adding subtext to reflect underlying tension” or “Tighten dialogue for a snappier flow.”

**Rating**: Conclude with a rating on a scale of 1-10 for dialogue and interactions, justifying your score. If the rating is below 9, specify key areas that need refinement to enhance the dialogue’s impact.

---

**Template for Response**:

"I have analyzed the dialogue and interactions with attention to the following aspects:
- **Dialogue Authenticity**: [Provide feedback here, e.g., “Most dialogue is realistic, but certain exchanges feel too expository.”]
- **Genre Consistency**: [Provide observations here, e.g., “The dialogue aligns well with the thriller genre, though some lines lack intensity.”]
- **Character Voice and Distinction**: [List any characters who need more distinctive voices and examples of strong character voice.]
- **Actionable Suggestions**: [Provide specific suggestions, like “Add subtle tension in character exchanges during key scenes.”]

**Rating**: Based on this evaluation, I would rate the dialogue and interactions **[8/10]**. To improve this score, I recommend [specific adjustments or refinements].
"""

    return dialogue_interactions
    
# Function to evaluate subplots and themes
def prompt_subplots_themes(data):
    subplots_themes=f"""You are a Story Consultant specializing in Themes and Subplots. Your task is to analyze the following script:\n\n"{data}"

**Focus**: Subplots and Themes. Provide positive reinforcement and constructive, empathetic guidance. Begin by highlighting what works well, then offer suggestions for refinement, emphasizing how the subplots and themes contribute to the overall story.

**Guidelines for Evaluation**:

1. **Define Main Themes**: Identify the script’s central themes—what big ideas or messages are explored (e.g., love, revenge, freedom, identity)? Assess if these primary themes are clear and resonate with the protagonist’s journey and the main plot. Offer feedback on how effectively these themes are communicated and integrated into the story.

2. **Supporting Themes**: Identify any secondary themes that complement or contrast the main themes. Do these add depth and richness to the story without overwhelming it? Provide feedback on how these supporting themes enhance the narrative or offer fresh perspectives on the central themes.

3. **Subplots and Their Integration**: Examine the subplots to determine if they connect meaningfully with the main plot. Do they enhance the story, or do they feel tangential? Evaluate if subplots are well integrated into the narrative without distracting from the protagonist’s journey.

4. **Character Growth and Complexity**: Assess whether the subplots provide opportunities for character development. Do they allow the protagonist or other characters to grow, change, or reveal new dimensions? Analyze how the subplots impact the characters’ journeys and add complexity to the story.

5. **Timing and Resolution**: Evaluate the pacing of the subplots. Are they introduced, developed, and resolved at appropriate moments in the story? Consider if they enhance the main plot or provide well-timed moments of relief, tension, or added complexity.

**Constructive Feedback**: Provide feedback on the strengths of the themes and subplots, as well as any areas that could be improved.

**Rating**: Conclude with a rating on a scale of 1-10 for the script’s subplots and themes, justifying your score. If the rating is below 9, suggest specific improvements to strengthen the integration and impact of the subplots and themes.

---

**Template for Response**:

"I have analyzed the themes and subplots with a focus on the following aspects:
- **Main Themes**: [Describe the central themes and how effectively they are portrayed, e.g., "The theme of identity is compelling and well-integrated with the protagonist’s journey."]
- **Supporting Themes**: [Provide insights, such as “The secondary theme of friendship enhances the main theme without overshadowing it.”]
- **Subplots and Integration**: [Evaluate the role and integration of subplots, with observations like “The subplot involving the protagonist’s friend adds depth but could be tied more closely to the main plot.”]
- **Character Growth and Complexity**: [Mention any ways in which subplots add layers to character development.]
- **Timing and Resolution**: [Assess the pacing of subplots, e.g., “The subplot is resolved too early, missing an opportunity for tension.”]

**Rating**: Based on this analysis, I would rate the subplots and themes **[8/10]**. To strengthen the impact, I recommend [specific improvements or adjustments here].
"""

    return subplots_themes
    
    
    
# Function to evaluate originality and creativity
def prompt_originality_creativity(data):
    originality_creativity=f"""You are a Script Evaluator with expertise in Originality and Creativity. Your task is to analyze the following script:\n\n"{data}"

**Focus**: Originality and Inventiveness. Provide blunt, no-nonsense feedback that identifies weaknesses and areas where the story could be more inventive. Be direct, addressing core issues and offering clear solutions to improve the script's uniqueness.

**Guidelines for Evaluation**:

1. **Unique Premise**: Assess whether the central idea presents a fresh or unusual concept. Is the story’s premise original, or does it feel like a rehash of familiar ideas? If the premise lacks uniqueness, suggest ways it can be made more distinctive or offer a new angle on a well-known trope.

2. **Plot Twists and Surprises**: Evaluate originality in the story’s progression. Are there plot developments or twists that challenge the audience’s expectations? If the plot feels predictable—especially in Act 3—offer ideas to introduce more unexpected or inventive elements to keep the audience engaged.

3. **Dialogue for Creativity**: Analyze the dialogue for freshness and inventiveness. Does it reflect each character’s voice in a distinctive and engaging way? If the dialogue feels generic or lacks creativity, provide specific examples and suggest ways to make it more unique and aligned with each character’s personality.

**Constructive Feedback**: Provide clear, direct feedback on the originality and creativity of the script, highlighting areas needing improvement and suggestions for enhancing its uniqueness.

**Rating**: Conclude with a rating on a scale of 1-10, justifying your score. If the rating is below 9, specify which elements—such as premise, plot twists, or dialogue—could benefit from more originality and provide concrete improvement ideas.

---

**Template for Response**:

"I have analyzed the script’s originality and creativity with attention to the following aspects:
- **Unique Premise**: [Provide your assessment here, e.g., “The premise is engaging but could benefit from a more unique angle, such as exploring a fresh motivation for the protagonist.”]
- **Plot Twists and Surprises**: [Provide observations here, e.g., “The story could introduce more surprises in Act 3 to avoid predictability.”]
- **Dialogue for Creativity**: [Highlight any areas where the dialogue lacks originality, providing suggestions for improvement, like “Add character-specific quirks in dialogue to make it more memorable.”]

**Rating**: Based on this analysis, I would rate the script **[7/10]**. To improve this score, I recommend [suggest specific adjustments, such as unique plot elements or more creative dialogue styles].
"""

    return originality_creativity
    
    
def lambda_handler(event, context):
    # Step 1: Get the data (Assuming it's passed in the event or fetched from a source)
    if isinstance(event, str):  # Check if event is a JSON string
        event = json.loads(event)  # Parse JSON string to dictionary
    
    data = json.dumps(event, ensure_ascii=False)
    print('printing data', data)
    
    # Step 2: Generate prompts using the defined functions
    prompts = [
        ("plot_structure", prompt_plot_structure(data)),
        #("character_development", prompt_character_development(data)),
        #("dialogue_interactions", prompt_dialogue_interactions(data))
        #("subplots_themes", prompt_subplots_themes(data)),
        #("originality_creativity", prompt_originality_creativity(data))

    ]
    
    # Step 3: Send each prompt to Bedrock and collect responses
    responses = []
    for func_name,prompt in prompts:
        response = lambda_client.invoke(
            FunctionName='arn:aws:lambda:eu-west-2:039612872581:function:call_bedrock',
            InvocationType='RequestResponse',
            #Payload=json.dumps({'prompt': prompt})  # Pass prompt as JSON object
            Payload=json.dumps({
        'prompt': prompt,
        'function_name': func_name  # Pass the function name if necessary
        })
        )
        
        # Read and parse the response from the Bedrock Lambda function
        response_payload = json.loads(response['Payload'].read())
        responses.append({
        'function_name': func_name,
        'response': response_payload
    })


    # Step 4: Return all responses in the final output
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Evaluations passed!',
        
        })
    }
