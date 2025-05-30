
import json
import os # 导入 os 模块用于检查文件是否存在
from openai import OpenAI
import json

def append_data_to_txt(file_path, new_data):
    """
    将一个 Python 字典（或列表）作为独立的 JSON 对象追加到文本文件（.txt）。

    Args:
        file_path (str): 要写入的文本文件路径。
        new_data (dict or list): 要追加的数据（一个 Python 字典或列表）。
    """
    try:
        # 将新数据转换为 JSON 格式字符串，注意 ensure_ascii=False 处理中文
        json_string = json.dumps(new_data, ensure_ascii=False)

        # 使用追加模式 'a' 打开文件，并添加换行符
        # 'a' 模式会在文件末尾追加内容
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(json_string + '\n')  # 写入 JSON 字符串，并加上换行符

        print(f"数据已追加到 {file_path}")

    except IOError as e:
        print(f"写入文件时发生 I/O 错误: {e}")
    except Exception as e:
        print(f"发生其他错误: {e}")




def read_json_lines(file_path):
  """
  读取 JSON Lines 文件，每行作为一个独立的 JSON 对象。

  Args:
      file_path (str): JSON Lines 文件的路径。

  Returns:
      list: 包含所有 JSON 对象的列表。
  """

  data = []
  with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
      # 每行都是一个独立的 JSON 对象，使用 json.loads() 解析
      data.append(json.loads(line.strip()))  # strip() 去掉可能存在的换行符
  all_name = [i.get('name') for i in data]
  return all_name

if __name__ == "__main__":
    new_json_file = 'new_new_speakers.json'
    client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="sk-jsha-1234567890")
    all_speakers = [
    {
      "id": "quentin-adam",
      "name": "Quentin Adam",
      "bio": "",
      "role": "",
      "org": "CleverCloud",
      "roleOrg": "CleverCloud",
      "image": "quentin-adam.png",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "sray-agarwal",
      "name": "Sray Agarwal",
      "bio": "Sray Agarwal has applied AI and analytics from Financial Services to Hospitality and has led the development of Responsible AI framework for multiple banks in the UK and the US.  Based out of London, his is conversant in Predictive Modelling, Forecasting and advanced Machine Learning with profound knowledge of algorithms and advanced statistic, Sray is Head of Responsible AI (EMEA & APAC) at Infosys. He is an active blogger and has given his talks on Ethical AI at major AI conferences across the globe (more than 20) and has podcasts, video interviews and lectures on reputed websites and social media at United Nations, Microsoft, ODSC to name a few. His contribution to the development of the technology was recognised by Microsoft when he won the Most Valued Professional in AI award in 2020 to 2025. He is also an expert for United Nations (UNCEFACT) and have recently authored a book on Responsible AI published by Springer.  He has been a trainer with leading consulting firms and have delivered training on business transformation using AI. He is guest lecturer at Jio institute. He holds patents on RAI system and methods.\r\n",
      "role": "Head of Responsible AI (EMEA & APAC)",
      "org": "Infosys",
      "roleOrg": "Head of Responsible AI (EMEA & APAC) at Infosys",
      "image": "sray-agarwal.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/srayagarwal/",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "luca-antiga",
      "name": "Luca Antiga",
      "bio": "",
      "role": "CTO",
      "org": "Lightning AI",
      "roleOrg": "CTO at Lightning AI",
      "image": "luca-antiga.jpeg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "rik-arends",
      "tag": "ai-apps",
      "name": "Rik Arends",
      "roleOrg": "Co-Founder of Makepad",
      "bio": "With 20+ years’ experience as a C/C++, JavaScript and more recently Rust developer, I've always been excited by using computation for visuals and audio. For this to work you need performance, and a smooth workflow enabled by the right tooling. After having everything I wanted with C except stable code I moved to JavaScript and web technologies. However, this never got to the point of being able to make fast applications that use modern CPU and GPU power. Now with Rust we have a new chance. I've been an entrepreneur my entire life building VJ software in the 00's, then web UI technology and web IDEs with Cloud9, and am now reimagining the developer workflow in Rust with Makepad. And lately how to leverage AI to write Rust and UI code.\r\n",
      "image": "rik-arends.png",
      "org": "Makepad",
      "role": "Founder",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/rikarends",
        "github": "https://github.com/makepad/makepad",
        "linkedin": "https://www.linkedin.com/in/arendsrik/",
        "website": "https://makepad.nl"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "catherine-arnett",
      "name": "Catherine Arnett",
      "bio": "",
      "role": "NPL Researcher",
      "org": "EleutherAI",
      "roleOrg": "NPL Researcher at EleutherAI",
      "image": "catherine-arnett.jpg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "elie-bakouch",
      "tag": "ai-model",
      "name": "Elie Bakouch",
      "roleOrg": "Research Engineer at Hugging Face",
      "bio": "Research Engineer focus on training LLMs at Hugging Face",
      "image": "elie-bakouch.jpeg",
      "org": "Hugging Face",
      "role": "Research Engineer",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/eliebakouch",
        "github": "https://github.com/eliebak",
        "linkedin": "https://www.linkedin.com/in/eliebak/",
        "website": "https://huggingface.co/eliebak"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "meriem-bendris",
      "name": "Meriem Bendris",
      "bio": "",
      "role": "Conversational AI Solutions Architect Manager",
      "org": "NVIDIA",
      "roleOrg": "Conversational AI Solutions Architect Manager at NVIDIA",
      "image": "meriem-bendris.jpg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "manuel-betin",
      "name": "Manuel Bétin",
      "bio": "",
      "role": "",
      "org": "OCDE",
      "roleOrg": "Economist, OCDE",
      "image": "manuel-bétin.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "guillaume-blaquiere",
      "name": "Guillaume Blaquiere",
      "bio": "Guillaume is a Google Developer Expert on Cloud Platform since 2019 and works at Carrefour as Group Data Architect. \r\n\r\nJava developer for more than 15 years, and despite positions of responsibilities, he has always kept his wish to create, develop, discover and test new solutions, especially in the Cloud, the machine learning or Python and Go language. \r\n\r\nInnovation addict and Google Cloud 3x certified, writer and speaker in his free time, he's fascinated by the serverless solution and all the \"usual\" problems that it solves.\r\n\r\nMore generally, he likes helping people stuck on Google Cloud; you can find him on Stack Overflow (guillaume-blaquiere), Medium (@guillaume-blaquiere) and Twitter (@gblaquiere)",
      "role": "Group Data Architect",
      "org": "Carrefour",
      "roleOrg": "Group Data Architect at Carrefour",
      "image": "guillaume-blaquiere.png",
      "tag": "ai-infra",
      "socialLinks": {
        "mastodon": "gblaquiere",
        "twitter": "https://x.com/gblaquiere",
        "github": "https://github.com/guillaumeblaquiere",
        "linkedin": "https://www.linkedin.com/in/guillaume-blaquiere",
        "website": "https://medium.com/@guillaume-blaquiere"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "gael-blondelle",
      "name": "Gaël Blondelle",
      "bio": "",
      "role": "",
      "org": "Eclipse Foundation",
      "roleOrg": "VP of the Eclipse Foundation",
      "image": "gael-blondelle.png",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "dongjie-chen",
      "name": "Dongjie Chen",
      "bio": "2021--2025 Huawei Programming Language Laboratory Software Engineer\r\nEngaged in the development of the Cangjie programming language, serving as the key contributor for concurrent programming design and AI programming design",
      "role": "Software Engineer",
      "org": "Huawei",
      "roleOrg": "Software Engineer at Huawei",
      "image": "dongjie-chen.jpg",
      "tag": "ai-apps",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "cheng-chi",
      "tag": "embodied-ai",
      "name": "Cheng Chi",
      "roleOrg": "Researcher at BAAI",
      "bio": "I am a researcher at the Beijing Academy of Artificial Intelligence (BAAI), focusing on embodied AI. My work explores large-scale multimodal models and cognitive architectures to enhance the perception, reasoning, and control capabilities of embodied AI systems.",
      "image": "cheng-chi.jpeg",
      "org": "BAAI",
      "role": "Researcher",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "https://chicheng123.github.io/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "wenjing-chu",
      "name": "Wenjing Chu",
      "bio": "Wenjing leads Futurewei's technology strategy on AI and Human Trust. He is an experienced technologist with a broad career spanning Internet, digital trust & security, and AI technologies.  He is the chair of the AI and Human Trust Working Group (AIMWG) in the Trust over IP (ToIP) project. AIMWG is developing a technical stack for trust in autonomous AI agents such as systems for identity, communication, delegation and accountability of AI agents. As a founding governing board member and a TAC member of the OpenWallet Foundation (OWF), he champions the development of AI digital trust technology available for everyone around the world. He has contributed significantly to the ToIP project of the LF Decentralized Trust community, authoring the Trust Spanning Protocol (TSP) Specification and the related technologies. Wenjing has long been an advocate and leader in the development of trustworthy AI, underpinned by a solid foundation of authenticity and digital trust.",
      "role": "Senior Director of Technology Strategy",
      "org": "Futurewei Technologies, Inc.",
      "roleOrg": "Senior Director of Technology Strategy at Futurewei Technologies, Inc.",
      "image": "wenjing-chu.png",
      "tag": "ai-apps",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/wenjingchu/",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "angelo-corsaro",
      "name": "Angelo Corsaro",
      "bio": "Angelo Corsaro, Ph.D.\r\nCEO, CTO, and Co-Founder of ZettaScale Technology\r\n\r\nAngelo Corsaro, Ph.D., is the Chief Executive Officer (CEO), Chief Technology Officer (CTO), and co-founder of ZettaScale Technology. At ZettaScale, he leads a world-class team dedicated to revolutionizing distributed computing, ensuring that every connected human and machine can communicate, compute, and store data anywhere, at any scale, efficiently, and securely.\r\n\r\nA globally recognized expert in Cloud-to-Thing Continuum, high-performance distributed systems, and real-time computing, Angelo is the inventor of the Zenoh protocol and the lead of the Eclipse Zenoh project. His work is reshaping the future of data-centric and event-driven architectures, bridging the gap between cloud, edge, and embedded systems.\r\n\r\nWith a prolific research background, Angelo has authored over 100 publications in peer-reviewed journals, conferences, workshops, and industry magazines. He has also contributed to over ten international standards, shaping the evolution of real-time and large-scale distributed computing.\r\n\r\nAngelo was a founding Co-Chair of the OMG DDS standard, playing a key role in its development and adoption. His leadership in DDS continued until 2015, when he stepped away due to technical divergences and committed himself to designing and implementing the first Zenoh protocol, paving the way for the next generation of data-centric middleware.",
      "role": "CEO/CTO",
      "org": "ZettaScale",
      "roleOrg": "CEO/CTO of ZettaScale",
      "image": "angelo-corsaro.png",
      "tag": "embodied-ai",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/acorsaro",
        "github": "http://github.com/kydos",
        "linkedin": "https://www.linkedin.com/in/corsaro/",
        "website": "https:/zettascale.tech"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "roberto-di-cosmo",
      "name": "Roberto Di Cosmo",
      "bio": "Roberto Di Cosmo is a computer scientist whose recent work bridges AI and software. After a career in programming languages and formal methods, he now focuses on large-scale software analysis and code transparency. A long-time advocate of Free Software, he founded and directs Software Heritage, the largest archive of public source code, used today to train responsible AI models. He also chairs the Software chapter of France’s National Committee for Open Science and sits on the board of the IMDEA Software Institute.",
      "role": "Director",
      "org": "Software Heritage / Inria",
      "roleOrg": "Director at Software Heritage / Inria",
      "image": "roberto-di-cosmo.png",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/rdicosmo",
        "github": "https://github.com/rdicosmo",
        "linkedin": "https://www.linkedin.com/in/roberto-di-cosmo/",
        "website": "https://dicosmo.org"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "sebastien-crozet",
      "name": "Sebastien Crozet",
      "bio": "Sébastien Crozet has been in love with the Rust programming language since its earliest days. He is the creator and maintainer of popular open-source libraries, including nalgebra and Rapier, for the Rust ecosystem that specialize in linear algebra, geometry, physics, and AI. He is the founder of Dimforge where he focuses on developing the future of AI, geometry and physics for engineering, games, and the metaverse.",
      "role": "CEO",
      "org": "Dimforge",
      "roleOrg": "CEO at Dimforge",
      "image": "sebastien-crozet.jpeg",
      "tag": "ai-infra",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "https://github.com/dimforge",
        "linkedin": "undefined",
        "website": "https://dimforge.com"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "nicolas-flores-herr",
      "name": "Nicolas Flores-Herr",
      "bio": "I'm Nicolas Flores Herr team lead at the Fraunhofer IAIS site in Dresden focused on training open-source generative AI models like Teuken. While we develop tailored AI solutions across industries our core passion lies in building and training large language and multilingual models from the ground up.\r\n\r\nWe work extensively on continued pretraining, fine-tuning, and instruction tuning, using both established frameworks and our own RAG-based technology stack. \r\n\r\nMuch of this work takes place in the context of leading European AI initiatives, including:\r\n\r\nOpenGPT-X – building large-scale, trustworthy, and open LLM “Made in Germany” called Teuken\r\nEuroLingua-GPT – training models that support all official European languages to foster digital inclusion.\r\nTrustLLM – advancing transparent and culturally sensitive AI for European languages and use cases.\r\nOpenEuroLLM – developing multilingual, open-source language models aligned with EU values and regulations.\r\n\r\nMy background is in physics (PhD), with over a decade of research experience in neuroscience and cell physiology. ",
      "role": "Team Lead Foundation Models",
      "org": "Fraunhofer IAIS",
      "roleOrg": "Team Lead Foundation Models at Fraunhofer IAIS",
      "image": "nicolas-flores-herr.jpeg",
      "tag": "ai-model",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "https://github.com/Modalities/modalities",
        "linkedin": "https://www.linkedin.com/in/floresherr/",
        "website": "https://huggingface.co/openGPT-X"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "pierre-gaillard",
      "name": "Pierre Gaillard",
      "bio": "He holds a Ph.D. in Machine Learning from the University of Technology of Compiègne, along with engineering and master's degrees in computer science and information systems. With over a decade of experience leading data-driven innovation, he thrives on bridging the gap between advanced data processing, artificial intelligence, and real-world industrial applications. Currently program manager at CEA, he leads the DeepGreen project, an initiative to develop Eclipse Aidge, an open source platform dedicated to embedded AI.",
      "role": "Embedded AI Program Manager",
      "org": "CEA",
      "roleOrg": "Embedded AI Program Manager at CEA",
      "image": "pierre-gaillard.png",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "erwan-gallen",
      "name": "Erwan Gallen",
      "bio": "",
      "role": "Senior Principal Product Manager",
      "org": "RedHat",
      "roleOrg": "Senior Principal Product Manager at RedHat",
      "image": "erwan-gallen.jpeg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "daniel-goldscheider",
      "name": "Daniel Goldscheider",
      "bio": "Daniel Goldscheider is founder and Executive Director of the OpenWallet Foundation and serves as Vice Chair of the Supervisory Board of Valamar Riviera d.d., Croatia’s largest tourism company. \r\n\r\nBefore that he started yes.com, an open banking scheme and co-founded Mediaguide with the American Society of Composers, Authors and Publishers as well as Aureus Private Equity (today Invision).",
      "role": "Executive Director",
      "org": "OpenWallet",
      "roleOrg": "Executive Director at the OpenWallet Foundation",
      "image": "daniel-goldscheider.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/goldscheider",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/goldscheider",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "garrett-goon",
      "name": "Garrett Goon",
      "bio": "",
      "role": "Research Scientist",
      "org": "IBM",
      "roleOrg": "Research Scientist at IBM",
      "image": "garrett-goon.jpeg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "donny-greenberg",
      "name": "Donny Greenberg",
      "bio": "Donny is the co-founder and CEO of 🏃‍♀️Runhouse🏠. He was previously the product lead for PyTorch at Meta, supporting the AI community across research, production, OSS, and enterprise. Notable projects include TorchRec, the open-sourcing of Meta's large-scale recommendations infra, TorchArrow & TorchData, PyTorch's next generation of data APIs, and unifying training infrastructure at Meta.",
      "role": "Co-founder / CEO",
      "org": "Runhouse",
      "roleOrg": "Co-founder / CEO at Runhouse",
      "image": "donny-greenberg.jpeg",
      "tag": "ai-infra",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/greenbergdon/",
        "website": "undefined"
      },
      "status": "New",
      "draft": True
    },
    {
      "id": "huy-hoang-ha",
      "tag": "ai-model",
      "name": "Huy Hoang Ha",
      "roleOrg": "LLM Researcher at Menlo Research",
      "bio": "Rex is a master’s student specializing in the Application of AI for Healthcare at Université Grenoble Alpes, France. His research focuses on developing a large language model (LLM) to assist clinicians while minimizing hallucinations. With a background in pharmacy, Rex is dedicated to bridging the gap between AI and domain-specific challenges in healthcare.\r\n\r\nRex is also a research scientist at Menlo Research, an open weights and data AI lab dedicated to optimizing intelligence per watt. At Menlo Research, he is working on early fusion speech models, enhancing their capabilities for low-resource languages and integration within robotic embodiments.",
      "image": "huy-hoang-ha.jpg",
      "org": "Menlo Research",
      "role": "LLM Researcher",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/HaHoang411",
        "github": "https://github.com/hahuyhoang411",
        "linkedin": "https://www.linkedin.com/in/hoanghavn/",
        "website": "https://menlo.ai/blog"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "yumei-he",
      "name": "Yumei He",
      "bio": "undefined",
      "role": "Assistant Professor",
      "org": "Tulane University",
      "roleOrg": "Assistant Professor at Tulane University",
      "image": "yumei-he.jpeg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/yumeihe/",
        "website": "https://freeman.tulane.edu/faculty-research/management-science/yumei-he"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "sirui-hong",
      "tag": "ai-apps",
      "name": "Sirui Hong",
      "roleOrg": "Co-Founder of DeepWisdom, MetaGPT/OpenManus Team Leader",
      "bio": "Sirui Hong is currently the technical leader of NLP/AIGC Algorithms at DeepWisdom (MetaGPT), responsible for algorithm research and development. She has experience in NLP, automated complex data analysis, and intelligent multi-agent system design. She won the NeurIPS 2019 AutoDL Competition (NLP track), authored the MetaGPT paper (ICLR 2024 Oral) and Data Interpreter paper, and co-authored the AFLOW paper (ICLR 2025 Oral). She is a core contributor to OpenManus. Her research has been published in TPAMI and ICLR, with current interests in enhancing large language models, advanced code generation, and multi-agent performance optimization.",
      "image": "sirui-hong.jpg",
      "org": "OpenManus",
      "role": "Technical Leader",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "https://scholar.google.com/citations?user=O-yMFdUAAAAJ&hl"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "florian-hnicke",
      "name": "Florian Hönicke",
      "bio": "Florian has 10 years of experience in the Field of AI, working at Axel-Springer, Deloitte, and SoundCloud. He works as a Principal Engineer at Jina AI, rapidly prototyping AI solutions. His expert domain is Agentic Search and synthetic data generation. Florian is serving as an AI policy advisor, providing explanations and insights to members of the European Parliament to enhance their understanding of artificial intelligence.",
      "role": "Principal AI Engineer",
      "org": "Jina AI",
      "roleOrg": "Principal AI Engineer at Jina AI",
      "image": "florian-hnicke.jpg",
      "tag": "ai-apps",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/florianhoenicke",
        "github": "https://github.com/florian-hoenicke",
        "linkedin": "https://www.linkedin.com/in/florian-h%C3%B6nicke-b902b6aa",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "dongxu-huang",
      "name": "Dongxu Huang",
      "bio": "Cofounder / CTO, TiDB",
      "role": "CTO",
      "org": "PingCAP",
      "roleOrg": "CTO at PingCAP",
      "image": "dongxu-huang.jpeg",
      "tag": "ai-infra",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/dxhuang",
        "github": "https://github.com/c4pt0r",
        "linkedin": "undefined",
        "website": "https://me.0xffff.me"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "jack-huang",
      "name": "Jack Huang",
      "bio": "Jack Huang is the Chairman and CEO of Gizwits, a well-known Chinese IoT solutions company. He holds an EMBA from Columbia University and London Business School, and a Bachelor's degree in Computer Science from the University of Kentucky in the United States. As a serial entrepreneur in the TMT (Technology, Media, and Telecommunications) sector and a Chinese-American entrepreneur who returned to China after studying in the US, Jack Huang is a representative figure in the field of IoT cloud services. He has been engaged in research and application work in TMT-related industries for many years and has unique insights and practical experience in using IoT to transform traditional industries. In 2014, he launched China's first IoT self-service development platform, pioneering the operation of an IoT developer ecosystem. He has been selected as one of the 100 Most Creative Business Figures in China by Fast Company, and one of the Top 30 Leaders in China's Globalization and Overseas Expansion by Forbes China.",
      "role": "Chairman & CEO",
      "org": "Gizwits",
      "roleOrg": "Chairman & CEO at Gizwits",
      "image": "jack-huang.jpg",
      "tag": "embodied-ai",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "https://www.gizwits.com"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "nicolas-hug",
      "name": "Nicolas Hug",
      "bio": "",
      "role": "ML Research Engineer",
      "org": "Meta",
      "roleOrg": "ML Research Engineer at Meta",
      "image": "nicolas-hug.jpg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "chao-jia",
      "name": "Chao Jia",
      "bio": "Jia Chao, Co-initiator of OpenBMB open-source community and Founding Partner of ModelBest. He led the organizational work for open-sourcing the entire series of ModelBest's MiniCPM on-device models. MiniCPM, nicknamed 'ModelBest's Little Steel Cannon'—which includes the large language model MiniCPM and the multimodal large model MiniCPM-V—has gained widespread recognition in the global AI community due to its highly efficient and cost-effective nature, embodying the principle of 'punching above its weight'  These projects have cumulatively received over 26,000 stars on GitHub, with total downloads exceeding 7 million across the web, becoming benchmark works in the field of on-device AI. ",
      "role": "Founding Partner",
      "org": "OpenBMB&Modelbest",
      "roleOrg": "Founding Partner at OpenBMB & Modelbest",
      "image": "chao-jia.jpg",
      "tag": "ai-model",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "jenia-jitsev",
      "name": "Jenia Jitsev",
      "bio": "Scientific lead and co-founder at LAION. Open foundation models and datasets necessary for their creation, studying generalist transferable learning and its scaling laws. Machine learning and neuroscience. Senior researcher and lab leader at Juelich Supercomputer Center (JSC), Research Center Juelich, Helmholtz Association ",
      "role": "Scientific lead",
      "org": "LAION; Juelich Supercomputing Center, Research Center Juelich",
      "roleOrg": "Scientific lead at LAION; Juelich Supercomputing Center, Research Center Juelich",
      "image": "jenia-jitsev.jpeg",
      "tag": "ai-model",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "arun-joseph",
      "name": "Arun Joseph",
      "bio": "",
      "role": "Head of AI Engineering",
      "org": "Deutsche Telekom",
      "roleOrg": "Head of AI Engineering at Deutsche Telekom",
      "image": "arun-joseph.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "christian-keller",
      "name": "Christian Keller",
      "bio": "",
      "role": "Product Lead - Generative AI Research",
      "org": "Meta",
      "roleOrg": "Product Lead - Generative AI Research at Meta",
      "image": "christian-keller.jpeg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "alexy-khrabrov",
      "tag": "ai-apps",
      "name": "Alexy Khrabrov",
      "roleOrg": "AI Community Architect at Neo4j",
      "bio": "Alexy Khrabrov is the AI Community Architect at Neo4j, the category-defining Graph database company. Alexy is the founding Chair of Open-Source Science at NumFOCUS, and a cofounder of the AI Alliance. Alexy was the founding Chair of the Generative AI Commons at the Linux Foundation for AI and Data (LFAI) and now represents Neo4j at LFAI.  Alexy is the founder and organizer of Bay Area AI and AI Agent SF meetups, as well as the Scale/Data/AI By the Bay conferences, the independent OSS AI conference running since 2013.\r\n\r\nPreviously, Alexy was the Director of Open-Source Science at IBM Research, a Technical Ecosystem Development Lead at IBM Quantum, Chief Scientist at Nitro, an Australian public company, a software engineer at Amazon, and a co-founder and engineer at several Bay Area startups. Dr. Khrabrov is an experienced community steward, founder and organizer, having created and run multiple meetups and open-source conferences in San Francisco Bay Area and around the world. Dr. Khrabrov's work is focused in community stewardship building distributed systems for AI applications, functional programming, and OSS ecosystems. Alexy cofounded the IEEE Open-Source Science Symposium, Scale, Data, and AI By the Bay conferences, and the Bay Area AI meetup, the longest-running and deepest technical AI meetup in the world.",
      "image": "alexy-khrabrov.jpg",
      "org": "Neo4j",
      "role": "AI Community Architect",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/chiefscientist",
        "github": "https://github.com/alexy",
        "linkedin": "https://www.linkedin.com/in/chiefscientist/",
        "website": "https://chiefscientist.org"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "ville-kuosmanen",
      "tag": "embodied-ai",
      "name": "Ville Kuosmanen",
      "roleOrg": "Founder at Voyage Robotics",
      "bio": "Ville is the founder of Voyage Robotics, a London-based Embodied AI startup.\r\n\r\nVille's recent open-source contributions focus on improving the capabilities and usability of open source robot AI, with a particular focus on tooling and fine-tuning around large VLA robotics foundation models, as well as spreading knowledge on the topic through a \"build in public\" lens.",
      "image": "ville-kuosmanen.jpg",
      "org": "Voyage Robotics",
      "role": "Founder",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/VilleKuosmanen",
        "github": "https://github.com/villekuosmanen",
        "linkedin": "https://www.linkedin.com/in/ville-kuosmanen-891889154/",
        "website": "https://villekuosmanen.com/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "eldar-kurtic",
      "name": "Eldar Kurtic",
      "bio": "",
      "role": "Senior ML Research Engineer",
      "org": "RedHat",
      "roleOrg": "Senior ML Research Engineer at RedHat",
      "image": "eldar-kurtic.jpeg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "yann-lechelle",
      "name": "Yann Lechelle",
      "bio": "",
      "role": "",
      "org": "Probabl.ai",
      "roleOrg": "Co-founder CEO at Probabl.ai",
      "image": "yann-lechelle.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "guohao-li",
      "tag": "ai-apps",
      "name": "Guohao Li",
      "roleOrg": "Founder and CEO of Eigent.AI / CAMEL-AI.org",
      "bio": "Guohao Li is the founder and CEO of Eigent.AI. He is an artificial intelligence researcher and an open-source contributor working on building intelligent agents that can perceive, learn, communicate, reason, and act. He is the core lead of the open source projects CAMEL-AI.org and DeepGCNs.org.\r\n\r\nGuohao Li was a postdoctoral researcher at University of Oxford with Prof. Philip Torr. He obtained his PhD degree in Computer Science at King Abdullah University of Science and Technology (KAUST) advised by Prof. Bernard Ghanem. During his Ph.D. studies, he was fortunate to work at Intel ISL with Dr. Vladlen Koltun and Dr. Matthias Müller as a research intern. He visited ETHz CVL as a visiting researcher. He also worked at Kumo AI and PyG.org with Prof. Jure Leskovec and Dr. Matthias Fey as a PhD intern. His primary research interests include Autonomous Agents, Graph Machine Learning, Computer Vision, and Embodied AI. He has published related papers in top-tier conferences and journals such as ICCV, CVPR, ICML, NeurIPS, RSS, 3DV, and TPAMI.",
      "image": "guohao-li.jpg",
      "org": "Eigent.AI / CAMEL-AI.org",
      "role": "Founder and CEO",
      "socialLinks": {
        "mastodon": None,
        "twitter": "https://x.com/guohao_li",
        "github": "https://github.com/lightaime",
        "linkedin": "https://www.linkedin.com/in/guohao-li-9a573b136/",
        "website": "https://ghli.org/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "jason-li",
      "tag": "ai-model",
      "name": "Jason Li",
      "roleOrg": "Senior VP at CSDN",
      "bio": "Jason Li, Senior Vice President of CSDN, Chief Technical Expert of Boolan, Chairman of Machine Learning Summit (ML-Summit) , and member of the ISO-C++ Standard Committee. He has rich experience and in-depth research in artificial intelligence, software architecture and product innovation. In recent years, he has mainly focused on the application of artificial intelligence methods centered around large language models. He proposed the \"ParaShift Cube\" for technological product innovation, and his related research and speeches have attracted strong attention from the industry. He provides high-end product innovation and technology strategy consulting services for well-known brands, including many Fortune Global 500 companies. He has been awarded the Microsoft Most Valuable Professional (MVP), Microsoft Regional Director and Tencent Most Valuable Professional (TVP) and other industry honorary titles for many times. He is a popular lecturer at many tech conferences and has taught a wide range of courses, including AI, software design, influencing more than one million technical professionals. He is also a serial entrepreneur who has founded well-known technology companies such as SoftCompass, SlideIdea, and Boolan.",
      "image": "jason-li.png",
      "org": "CSDN",
      "role": "Senior Vice President",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/jianzhongli/",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "yongbin-li",
      "tag": "ai-apps",
      "name": "Yongbin Li",
      "roleOrg": "Senior Algorithm Expert at Alibaba Tongyi Lab",
      "bio": "Yongbin LI graduated from Tsinghua University and is a senior algorithm expert at Alibaba's TONGYI Lab. His research focuses on LLMs, including code models, character models, post-training and agents. He has developed the Tongyi Lingma coding copilot and AI programmer (coding agent), which is currently the largest and most popular coding product in China, and has recently launched the international version of Tongyi Lingma. Additionally, he is responsible for the LLM technologies such as Tongyi Xingchen (Character Model/Role-playing Agent), Tongyi Xiaomi (Intelligent Customer Service), and Tongyi Tingwu (Audio and Video Assistant). \r\nSince 2020, he has published over 90 papers in top international conferences (ICLR, NeurIPS, ICML, ACL, EMNLP, CVPR, etc.) on topics related to LLMs, code models and character models, achieving an H-index of 27. He has also served as a area chair for ACL, NAACL, and WSDM.",
      "image": "yongbin-li.png",
      "org": "Alibaba Tongyi Lab",
      "role": "Senior Algorithm Expert",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "https://yongbin-li.github.io/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "minglan-lin",
      "name": "Minglan Lin",
      "bio": "Minglan Lin possesses extensive expertise in training large models, including LLMs, VLMs, and embodied intelligence VLMs. At the BAAI Embodied Intelligence Team, Minglan spearheaded the development and open-sourcing of the RoboBrain large model and the hierarchical collaborative framework RoboOS.",
      "role": "Embodied Intelligence Researcher",
      "org": "BAAI",
      "roleOrg": "Embodied Intelligence Researcher at BAAI",
      "image": "minglan-lin.jpg",
      "tag": "embodied-ai",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "yonghua-lin",
      "tag": "ai-infra",
      "name": "Yonghua Lin",
      "roleOrg": "VP of BAAI",
      "bio": "Yonghua Lin is the Vice President and Chief Engineer of Beijing Academy of Artificial Intelligence, responsible for AI System, and Large Model Foundation Technology research, industry and open-source ecosystem cooperation.  She is formerly the Director of IBM China Research Lab and Distinguished Engineer at IBM, she led global AI system innovation within IBM.  She has been engaged in research on system architecture, cloud computing, AI systems, computer vision, and other fields for more than 20 years. She holds over 50 global patents and has won the ACM/IEEE Best Paper awards. She was named one of the \"50 Leading Female Tech Leaders in China\" by Forbes in 2019. She is member of IEEE Women in Engineering Asia Pacific Leadership Team and the founder of IEEE Women in Engineering Beijing affinity.",
      "image": "yonghua-lin.png",
      "org": "BAAI FlagGem",
      "role": "VP",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "volha-litvinets",
      "name": "Volha Litvinets",
      "bio": "As a Digital Ethics Lead at Ernst & Young Advisory, France, Volha (Olga) is experienced in innovation and Responsible Artificial Intelligence (AI). With a PhD in AI ethics from Sorbonne University and an INSEAD Business School diploma, she drives responsible technology initiatives, bringing a wealth of experience from the private sector, public sector and Non-Governmental Organizations (NGOs), having worked in strategy, development, research and education.\r\n\r\nAt the Global EY organization, Olga has led projects for key clients and developed methodologies focused on responsible AI and risk management. She led several workshops and published articles related to responsible AI and operational ethics and represented the organization at internal and external events.\r\n\r\nPreviously, Olga was a research fellow at the Carnegie Council for Ethics in International Affairs and analyzed lethal autonomous weapons conventions at the United Nations Office for Disarmament Affairs.\r\n\r\nOlga is at the forefront of integrating responsible AI practices within client operations. She employs a dual approach: driving top-down implementation of AI governance while fostering bottom-up engagement through AI literacy trainings. Her initiatives aim to raise awareness and to help ensure AI technologies are developed and deployed ethically and sustainably, aligned with human rights, to help clients navigate the complexities of AI responsibly, reinforcing core business values.",
      "role": "Digital Ethics Lead / Responsible AI",
      "org": "Ernst&Young Advisory",
      "roleOrg": "Digital Ethics Lead / Responsible AI at Ernst&Young Advisory",
      "image": "volha-litvinets.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/litvinets/",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "guang-liu",
      "tag": "ai-model",
      "name": "Guang Liu",
      "roleOrg": "Technical Lead of Data Research Team at BAAI",
      "bio": "Guang Liu, Technical Lead at BAAI's Data Research Team, directs the OpenSeek project. He is the architect behind the Aquila large language model series and the Infinity dataset family. His current research centers on Agentic Data Systems, innovating synthetic data generation for next-generation AI training.",
      "image": "guang-liu.jpg",
      "org": "BAAI",
      "role": "Technical Lead of Data Research Team",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "https://github.com/zacliu2023",
        "linkedin": "undefined",
        "website": "https://huggingface.co/ZacLiu"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "shiwei-liu",
      "tag": "ai-model",
      "name": "Shiwei Liu",
      "roleOrg": "Royal Society Newton International Fellow at University of Oxford",
      "bio": "Shiwei Liu is a Royal Society Newton International Fellow at the University of Oxford. He will join Max Planck Institute for Intelligent Systems as a group leader and ELLIS Institute Tubingen as a PI. He previously served as a Postdoctoral Fellow at the University of Texas at Austin. He obtained his Ph.D. with Cum Laude from Eindhoven University of Technology in 2022. His research focuses on leveraging, understanding, and expanding the role of sparsity and low-rank approximations in neural networks, whose impacts span many important topics, such as efficient training/inference/transfer of large-foundation models, robustness and trustworthiness, and generative AI. He received two Rising Star Awards from KAUST and the Conference on Parsimony and Learning (CPAL). ",
      "image": "shiwei-liu.jpg",
      "org": "University of Oxford",
      "role": "Royal Society Newton International Fellow",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/Shiwei_Liu66",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "https://shiweiliuiiiiiii.github.io/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "xinrui-liu",
      "tag": "ai-apps",
      "name": "Xinrui Liu",
      "roleOrg": "Developer Ecosystem Director at LangGenius",
      "bio": "Xinrui Liu, Developer Ecosystem Director at DIFY, is responsible for building DIFY's global open-source ecosystem partnership network and driving the deep integration of developer tools with commercial value.\r\n\r\nA graduate of Northwestern University, she specializes in designing commercialization pathways for open-source products and establishing compliance frameworks for open-source licenses. She is committed to finding a balance between community innovation and sustainable corporate growth.\r\n\r\nAs a next-generation AI-native application development platform, DIFY upholds the philosophy of open-source-driven innovation. Through technological empowerment, resource connectivity, and ecosystem incubation, DIFY aims to help developers and enterprises worldwide bridge the gap between code and commercial value.",
      "image": "xinrui-liu.jpg",
      "org": "LangGenius, Inc.",
      "role": "Developer Ecosystem Director",
      "socialLinks": {
        "mastodon": None,
        "twitter": None,
        "github": None,
        "linkedin": None,
        "website": None
      }
    },
    {
      "id": "remi-louf",
      "name": "Rémi Louf",
      "bio": "",
      "role": "Co-Founder and CEO",
      "org": "DotTXT",
      "roleOrg": "Co-Founder and CEO at DotTXT",
      "image": "remi-louf.png",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "yinping-ma",
      "tag": "ai-infra",
      "name": "Yinping Ma",
      "roleOrg": "Engineer at Peking University",
      "bio": "Deputy Leader of the Large Model Working Group at Peking University Computing Center, and Adjunct Associate Researcher at the PKU-Changsha Institute for Computing and Digital Economy. My primary research areas include high-performance computing（HPC）, intelligent computing, and computing power networks. I have been involved in the construction and management of multiple HPC clusters and has published over ten papers and dozens of patents in fields such as HPC scheduling, application optimization, high-performance operator optimization, and artificial intelligence. I led the development of the open source computing power scheduling system CraneSched and participated in the development of the computing center portal and management platform OpenSCOW. I have contributed to several major projects, including the National Key R&D Program of China under the \"New Generation Artificial Intelligence\" initiative, the Top Ten Technological Breakthrough Projects of Hunan Province, the Key R&D Program of Guangdong Province, and various Huawei university-industry collaboration projects.",
      "image": "yinping-ma.jpg",
      "org": "Peking University",
      "role": "Engineer",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "stefano-mafulli",
      "name": "Stefano Mafulli",
      "bio": "",
      "role": "",
      "org": "OSI",
      "roleOrg": "ED of the OSI",
      "image": "stefano-maffulli.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "michel-marie-maudet",
      "name": "Michel-Marie Maudet",
      "bio": "Michel-Marie MAUDET has led LINAGORA (https://www.linagora.com/) as its Managing Director and co-founder for almost 25 years. He is a pioneer in the world of the free software in France and Europe since thirty years.\r\n\r\nWith Artificial Intelligence becoming more common in our lives and the dominance of large tech companies like GAFAM, Michel-Marie sees the need for alternative technologies. In 2016, he launched LinTO (https://www.linto.ai/), an entirely Open Source personal assistant, reflecting his vision for open and accessible technology for everyone. \r\n\r\nIn June 2023, he started the OpenLLM France (https://www.openllm-france.fr/)  community. This community brings together experts to share knowledge and work together on developing a French, sovereign, and truly Open Source LLM. For us, truly Open Source requires three conditions :\r\n    • Open Source code\r\n        ◦ Source code of the code model, pre training tool released under OSI compliant Open Source Licence\r\n    • Open Model\r\n        ◦ Licence and user agreement without any restrictions on who may use it and for what \r\n    • Open Training Datasets\r\n        ◦ 100% of training data must be publicly available in a format that allows for investigation of the model's biases (preferences) and for retraining\r\n\r\nDuring the FOSDEM 2024, the OpenLLM France community has been changed to OpenLLM Europe in order to make possible the creation of digital commons in the field of Generative AI at European level by federating other national initiatives. \r\n\r\nIn the AI area, we need Digital Bioversity : Michel-Marie and LINAGORA work on this challenge by continuing to support open standards and aiming for an open, ethical, and responsible digital future.",
      "role": "General Manager",
      "org": "LINAGORA - OpenLLM France",
      "roleOrg": "General Manager at LINAGORA - OpenLLM France",
      "image": "michel-marie-maudet.png",
      "tag": "ai-model",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/mmaudet",
        "github": "https://github.com/mmaudet",
        "linkedin": "https://www.linkedin.com/in/mmaudet/",
        "website": "https://www.6sn.ai/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "pablo-montalvo",
      "name": "Pablo Montalvo",
      "bio": "",
      "role": "Machine Learning Engineer",
      "org": "Hugging Face",
      "roleOrg": "Machine Learning Engineer at Hugging Face",
      "image": "pablo-montalvo.jpeg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "jean-laurent-de-morlhon",
      "name": "Jean-Laurent de Morlhon",
      "bio": "Jean-Laurent de Morlhon is an Executive & SVP of Engineering at Docker, leading Generative AI initiatives to enhance the developer experience across the Docker ecosystem. With over nine years at Docker, he has played a key role in shaping its engineering culture, scaling teams, and driving innovation in cloud-native development. A seasoned engineering leader with deep expertise in developer tools, infrastructure, and software delivery, Jean-Laurent is passionate about automation, security, and AI-powered developer experiences. As an executive at Docker, he focuses on fostering high-performing teams, delivering impactful products, and pushing the boundaries of developer productivity. Beyond Docker, he actively engages with the tech community and shares his insights on Bluesky @morlhon.bsky.social. ",
      "role": "Sr Vice President, GenAI Acceleration",
      "org": "Docker",
      "roleOrg": "Sr Vice President, GenAI Acceleration at Docker ",
      "image": "jean-laurent-de-morlhon.png",
      "tag": "ai-infra",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/morlhon/",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "marianna-nezhurina",
      "name": "Marianna Nezhurina",
      "bio": "LAION core researcher, open foundation models and datasets",
      "role": "Researcher",
      "org": "Juelich Supercomputing Centre",
      "roleOrg": "Researcher at Juelich Supercomputing Centre",
      "image": "marianna-nezhurina.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "https://github.com/marianna13",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "hong-thai-nguyen",
      "name": "Hong-Thai Nguyen",
      "bio": "As an Engineering Manager at Cegid, I support and guide the development of Cegid Pulse OS, a cutting-edge platform designed to orchestrate seamless collaboration between humans and machines through intelligent agents. Leveraging large language models (LLMs) and advanced AI capabilities, the platform dynamically interprets user intent and executes tailored tasks with precision and efficiency.\r\n\r\nPreviously, I led the development of Cegid Concilator, a production-grade platform for automated invoice extraction and transformation using AI and OCR technologies. This solution helped streamline financial workflows by accurately parsing and processing complex invoice data at scale.\r\n\r\n🔧 Key responsibilities:\r\n- Enabling product teams to build production-ready agent systems, aligned with business needs and technical standards.\r\n\r\n- Promoting best practices in Prompt Engineering, LLM-friendly API design, and secure, privacy-conscious agent architecture.\r\n\r\n- Addressing LLM-specific challenges: debugging, improving observability, and enhancing explainability for trustworthy and transparent agent behavior.\r\n\r\n🚀 Passionate about applied AI, I focus on delivering impactful, intelligent solutions with production grade that elevate user experiences and transform enterprise workflows.",
      "role": "Software Engineering Manager",
      "org": "Cegid",
      "roleOrg": "Software Engineering Manager at Cegid",
      "image": "hong-thai-nguyen.jpg",
      "tag": "ai-apps",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "https://github.com/cegid",
        "linkedin": "https://www.linkedin.com/in/hong-thai-nguyen/",
        "website": "https://www.cegid.com/global/ai/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "ciaran-oriordan",
      "name": "Ciarán O'Riordan",
      "bio": "Senior Policy Advisor at OFE, Ciarán O’Riordan has been working in Brussels since 2004 with a focus on EU policy and free and open source software. His work in the sector includes copyright and patent policy in the EU, patent policy in the US, and community engagement for the drafting of version 3 of the GNU General Public License. He also brings policy experience from the automotive sector, GDPR, and corporate finance. He studied law at UCLouvain Saint-Louis Bruxelles. A user of GNU/Linux since 1998, Ciarán worked as a software developer in Dublin before his move to Brussels.",
      "role": "Senior Policy Advisor",
      "org": "OFE",
      "roleOrg": "Senior Policy Advisor at OFE",
      "image": "ciaran-oriordan.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "philipp-oppermann",
      "tag": "embodied-ai",
      "name": "Philipp Oppermann",
      "roleOrg": "Dora Project Lead",
      "bio": "Philipp Oppermann is a freelance Rust developer from Germany. He is working on the Dora robotic framework and on various projects related to operating system development in Rust. Philipp is the author of the \"Writing an OS in Rust\" blog and the main editor of the \"This Month in Rust OSDev\" newsletter.",
      "image": "philipp-oppermann.jpeg",
      "org": "DORA+Zenoh",
      "role": "-",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "https://github.com/phil-opp",
        "linkedin": "undefined",
        "website": "https://os.phil-opp.com"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "pedro-ortis",
      "name": "Pedro Ortis",
      "bio": "",
      "role": "Senior Research Scientist",
      "org": "Common Crawl",
      "roleOrg": "Senior Research Scientist at Common Crawl",
      "image": "pedro-ortis-suarez.jpg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "anne-charlotte-passanisi",
      "name": "Anne-Charlotte Passanisi",
      "bio": "Anne-Charlotte Passanisi is a Senior Product Manager at Pollen Robotics, where she explores how emotional design can help make robots more understandable, relatable, and accepted by humans. With over 10 years of experience in digital product development, from events and startups to gaming, she now focuses on how artificial empathy can support better adoption, engagement, and retention. She doesn’t build AI from scratch, but loves shaping the way people experience it.",
      "role": "Senior Product Manager",
      "org": "Pollen Robotics",
      "roleOrg": "Senior Product Manager at Pollen Robotics",
      "image": "annecharlotte-passanisi.png",
      "tag": "embodied-ai",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/pollenrobotics",
        "github": "https://github.com/pollen-robotics",
        "linkedin": "https://www.linkedin.com/in/annecharlottepassanisi/",
        "website": "https://www.pollen-robotics.com/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "guilherme-penedo",
      "tag": "ai-model",
      "name": "Guilherme Penedo",
      "roleOrg": "ML Research Engineer at Hugging Face",
      "bio": "Previously a member of the Falcon team, where he was in charge of creating the pretraining dataset for the first iteration of the Falcon LLM: RefinedWeb, Guilherme is now a member of the Hugging Face Science Team, where he works on improving pretraining datasets and led the FineWeb and FineWeb2 projects, two large scale datasets for LLM pretraining. More recently, he's been involved in Open-R1, Hugging Face's fully open effort to replicate the DeepSeek-R1 model.",
      "image": "guilherme-penedo.jpg",
      "org": "Hugging Face",
      "role": "ML Research Engineer",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/gui_penedo",
        "github": "https://github.com/guipenedo",
        "linkedin": "https://www.linkedin.com/in/guilhermepenedo",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "cailean-osborne",
      "name": "Cailean Osborne, PhD",
      "bio": "Cailean Osborne is a senior researcher at the Linux Foundation, who leads strategic research on open source AI. Cailean has a PhD in Social Data Science from the University of Oxford, where he researched commercial interests and collaboration dynamics in open source AI developer communities, and in 2023-2024 he was a visiting researcher at Peking University’s Open Source Software Data Analytics Lab. Previously, Cailean worked in AI policy at the UK Government and was a UK government delegate at the OECD’s Global Partnership on AI and the Council of Europe’s Committee on AI. Cailean is based in Berlin, Germany.",
      "role": "Senior Researcher",
      "org": "Linux Foundation",
      "roleOrg": "Senior Researcher at Linux Foundation",
      "image": "cailean-osborne.png",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/caileanosborne/",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "michael-plagge",
      "name": "Michael Plagge",
      "bio": "",
      "role": "",
      "org": "Eclipse Foundation",
      "roleOrg": "VP of the Eclipse Foundation",
      "image": "plagge-michael.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "diego-rojas",
      "name": "Diego Rojas",
      "roleOrg": "Research Engineer at Zhipu.AI",
      "bio": "Hacking on LLMs for Code at Zhipu.AI, THUKEG & Super Convergence",
      "role": "Research Engineer",
      "org": "Zhipu.AI",
      "image": "diego-rojas.jpeg",
      "tag": "ai-model",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/dhbrojas",
        "github": "https://github.com/dhbrojas",
        "linkedin": "https://www.linkedin.com/in/dhbrojas/",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "pierre-rouanet",
      "name": "Pierre Rouanet",
      "bio": "",
      "role": "Co-Founder & CTO",
      "org": "Pollen Robotics",
      "roleOrg": "Co-Founder & CTO at Pollen Robotics",
      "image": "pierre-rouanet.jpg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "martino-russi",
      "tag": "embodied-ai",
      "name": "Martino Russi",
      "roleOrg": "Embodied Robotics Engineer at Hugging Face",
      "bio": "Aspiring mad scientist, trying to create this generation's Pinocchio.  My background is interdisciplinary, spanning neuroscience, AI and robotics. My goal is to make embodied intelligence affordable for everyone.",
      "image": "martino-russi.jpeg",
      "org": "Hugging Face",
      "role": "Embodied robotics engineer",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://twitter.com/NepYope",
        "github": "https://github.com/nepyope/",
        "linkedin": "https://www.linkedin.com/in/martino-russi-a822081bb",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "olatunji-ruwase",
      "name": "Olatunji Ruwase",
      "bio": "",
      "role": "Deep Learnning Expert",
      "org": "Ex-SnowFlake",
      "roleOrg": "Deep Learnning Expert",
      "image": "olatunji-ruwase.jpeg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "joaquin-salvachua",
      "name": "Joaquin Salvachua",
      "bio": "Joaquín Salvachúa is a Professor at the Universidad Politécnica de Madrid, In the specializing in the Department of Telematics Systems Engineering at the Telecommunication School. He is a member of the board at Gaia-X Hub España, FIWARE and BDVA and active contributor in Gaia-X AISBL.  and actively participates in research on ML-OPS, Big data architectures, cloud computing, next-generation internet technologies, network science and formal methods. Has authored numerous academic publications.",
      "role": "Profesor Titular",
      "org": "Universidad Politecnica de Madrid",
      "roleOrg": "Profesor Titular at Universidad Politecnica de Madrid",
      "image": "joaquin-salvachua.jpeg",
      "tag": "assign-me",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://bsky.app/profile/jsalvachua.bsky.social",
        "github": "https://github.com/jsalvachua",
        "linkedin": "https://www.linkedin.com/in/jsalvachua/",
        "website": "https://portalcientifico.upm.es/es/ipublic/researcher/305315"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "greg-schoeninger",
      "tag": "ai-infra",
      "name": "Greg Schoeninger",
      "roleOrg": "CEO at Oxen.ai",
      "bio": "Founder and CEO of Oxen.ai, former IBM Watson. Have been training language models for over a decade. ",
      "image": "greg-schoeninger.jpeg",
      "org": "Oxen.ai",
      "role": "CEO",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/gregschoeninger",
        "github": "https://github.com/gschoeni",
        "linkedin": "undefined",
        "website": "https://www.oxen.ai/blog"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "hung-ying-tai",
      "name": "Hung-Ying Tai",
      "bio": "Hung-Ying, Tai (hydai) is the maintainer of the WasmEdge Runtime project and an engineering leader at Second State. He is a prolific mentor in the Linux Foundation Mentorship program and a CNCF Ambassador. He also contributes to many high-profile open source projects within and beyond the CNCF. He is knowledgeable about AI inference frameworks such as llama.cpp, PyTorch, and TensorFlow.",
      "role": "Engineering leader",
      "org": "Second State",
      "roleOrg": "Engineering Leader at Second State",
      "image": "hung-ying-tai.jpg",
      "tag": "ai-infra",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/hydai_tw",
        "github": "https://github.com/hydai",
        "linkedin": "undefined",
        "website": "https://hyd.ai"
      },
      "status": "New",
      "draft": True
    },
    {
      "id": "markus-tavenrath",
      "tag": "ai-infra",
      "name": "Markus Tavenrath",
      "roleOrg": "Principal Engineer Developer Technology at NVIDIA",
      "bio": "Markus Tavenrath studied computer science with a focus on computer graphics at RWTH Aachen University. This academic background provided a solid foundation for his career in the technology industry.\r\n\r\nIn 2008, Markus joined NVIDIA, where he began working on real-time ray tracing on GPUs. Over the years, he has contributed to performance optimization for ray tracing, scene graphs, OpenGL, WebGL, Vulkan, and AI. His work has played a role in advancing these technologies.\r\n\r\nMarkus is also a co-founder of the Vulkan-Hpp project, which has been beneficial to the Vulkan community. His efforts have helped improve the use and implementation of Vulkan.\r\n\r\nRecently, Markus was elected as the Chair of the ML Council at Khronos. In this role, he helps coordinate and support AI and machine learning initiatives within the Khronos group. His election to this position reflects his expertise and leadership qualities.\r\n\r\nMarkus Tavenrath is a dedicated professional whose contributions have positively impacted the technological landscape at NVIDIA and beyond.",
      "image": "markus-tavenrath.jpg",
      "org": "NVIDIA",
      "role": "Principal Engineer Developer Technology",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "https://www.linkedin.com/in/markus-tavenrath",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "nouamane-tazi",
      "name": "Nouamane Tazi",
      "bio": "",
      "role": "Machine Learning Engineer",
      "org": "Hugging Face",
      "roleOrg": "Machine Learning Engineer at Hugging Face",
      "image": "nouamane-tazi.jpeg",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "christian-tzolov",
      "name": "Christian Tzolov",
      "bio": "Christian Tzolov, R&D Software Engineer at Broadcom's Spring team, leads the Spring AI and MCP Java SDK projects. He specializes in connecting enterprise systems with AI capabilities, helping Java developers build intelligent applications. Christian brings hands-on experience and a pragmatic approach to making advanced AI concepts accessible and useful for real-world applications.",
      "role": "R&D Software Engineer",
      "org": "Spring team at Broadcom",
      "roleOrg": "R&D Software Engineer at Spring team at Broadcom",
      "image": "christian-tzolov.png",
      "tag": "ai-apps",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/christzolov",
        "github": "https://github.com/tzolov",
        "linkedin": "https://www.linkedin.com/in/tzolov/",
        "website": "https://spring.io/authors/tzolov"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "ovidiu-vermesan",
      "name": "Ovidiu Vermesan",
      "bio": "",
      "role": "",
      "org": "SINTEF",
      "roleOrg": "Chief Scientist at SINTEF",
      "image": "ovidiu-vermesan.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "qin-wang",
      "name": "Qin Wang",
      "bio": "Dr. Qin Wang holds the position of Senior Research Fellow at the Institute of Industrial Economics, Chinese Academy of Social Sciences, and is a Professor at the University of Chinese Academy of Social Sciences. He also serves as the Director of the Management Science and Innovation Development Centre at the Chinese Academy of Social Sciences and holds the role of Executive Vice Chairman at the China Enterprise Management Research Association. Professor Wang has dedicated an extensive period to researching innovation management and organizational change. His notable achievements include receiving the Second China Soft Science Award (Deep Research Award) and the Third Jiang Yiwei Enterprise Reform and Development Fund Works Award for his outstanding contributions. Professor Wang has published more than 100 articles in academic journals such as Harvard Business Review (Chinese version), Tsinghua Management Review, China Industrial Economy, and Economic Management. He has also authored various monographs, including \"The Transformation of China's Manufacturing Industry Driven by Information Network Technology,\" \"The Innovation Strategy of Chinese Enterprises,\" and \"RenDanHeYi Management\" (available in both Simplified and Traditional Chinese versions). In addition, he co-authored \"The Path of Independent Innovation with Chinese Characteristics\" and \"The Regional Innovation Systems in China,\" among others.",
      "role": "Professor",
      "org": "Chinese Academy of Social Sciences",
      "roleOrg": "Professor at Chinese Academy of Social Sciences",
      "image": "qin-wang.jpg",
      "tag": "forum",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "xiyuan-wang",
      "tag": "ai-infra",
      "name": "Xiyuan Wang",
      "roleOrg": "Senior Software Engineer at Huawei",
      "bio": "I have worked on OpenSource for over ten years.  I was Openstack Keystone project maintainer previously. And now I'm focus on opensource AI software.  I'm the maintainer of vllm-project/vllm-ascend currently",
      "image": "xiyuan-wang.jpeg",
      "org": "Huawei",
      "role": " 高级软件工程师 Gāojí ruǎnjiàn gōngchéngshī Senior software engineer",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "https://github.com/wangxiyuan",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "yanzhi-wang",
      "tag": "ai-model",
      "name": "Yanzhi Wang",
      "roleOrg": "Professor, Electrical and Computer Engineering at Northwestern University",
      "bio": "Yanzhi Wang is Professor in the Department of Electrical and Computer Engineering at Northeastern University, a senior member of IEEE. His research interests focus on real-time and energy-efficient deep learning and artificial intelligence systems, especially on efficient large language models and large-scale generative AI systems. His research works have been published broadly in (i) machine learning conferences such as AAAI, CVPR, NeurIPS, ICML, ICCV, ICLR, IJCAI, ECCV, KDD, ICRA, ACM MM, ICDM, etc., (ii) architecture and system conferences such as ASPLOS, ISCA, MICRO, HPCA, CCS, VLDB, PLDI, WWW, ICS, PACT, CGO, IPDPS, INFOCOM, ICDCS, DAC, ICCAD, FPGA, FCCM, ISSCC, CICC, RTAS, RTSS, etc., and (iii) IEEE and ACM transactions. His research works have been cited over 22,500 times. He has received six Best Paper Awards and another 12 Best Paper Nominations. He has received the U.S. Army Research Office Young Investigator Program Award (YIP), IEEE TC-SDM Early Career Award, Asia Pacific Signal and Information Processing Association Distinguished Leader Award, Massachusetts Acorn Innovation Award, design contest awards from multiple conferences, and other research awards from Google, MathWorks, etc. His research work has been reported and cited by around 500 media. He has 13 academic descendents as tenure-track faculty members at University of Minnesota, Michigan State University, University of Georgia, Clemson University, etc.\r\n",
      "image": "yanzhi-wang.png",
      "org": "Northeastern University",
      "role": "Professor",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "matt-white",
      "name": "Matt White",
      "role": "Executive Director",
      "roleOrg": "Executive Director, PyTorch Foundation. GM of AI, Linux Foundation.",
      "bio": "Matt White is the Executive Director of the PyTorch Foundation and GM of AI at the Linux Foundation, as well as the Director of the Generative AI Commons under the LF AI & Data Foundation. With nearly 30 years of experience in AI research, standards, and applications across telecom, media, and gaming, he has specialized since 2012 in machine learning, simulations, and multi-sensory learning. He previously co-founded the Open Metaverse Foundation, chairs the Metaverse Standards Forum, and co-organizes both the Silicon Valley Generative AI paper reading group and the GenAI Collective.",
      "image": "matt-white.png",
      "org": "PyTorch Foundation, Linux Foundation",
      "tag": "pytorch",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "baosong-yang",
      "tag": "ai-model",
      "name": "Baosong Yang",
      "roleOrg": "Scientist at Alibaba's Tongyi Lab",
      "bio": "Baosong Yang is a Scientist at Alibaba's Tongyi Lab, where he leads efforts to enhance the multilingual capabilities of the Qwen series models, including Qwen, Qwen-QwQ, Qwen-Audio, and Qwen-Omni. His team is also responsible for developing Alibaba's machine translation system, which is utilized over 1.7 billion times each day. Baosong earned his Ph.D. from the NLP2CT Lab at the University of Macau, specializing in multilingualism within the field of natural language processing (NLP). He has authored over 50 papers in prestigious NLP and AI journals and conferences, such as ACL, EMNLP, AAAI, and NeurIPS.",
      "image": "baosong-yang.png",
      "org": "Alibaba Tongyi Lab",
      "role": "Scientist",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "https://baosongyang.site/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "james-yang",
      "name": "James Yang",
      "bio": "James Yang holds a PhD from the University of Pennsylvania, a master's degree from Rice University, and a bachelor's degree from the University of Science and Technology of China. He is the Founder and CEO of Synkrotron Inc and a professor at the University of Science and Technology of China. He served as a professor in the Department of Computer Science at Western Michigan University and a visiting professor in the Department of Electrical Engineering and Computer Science at the University of Michigan. Currently he is a co-Chair of the IEEE Electric and Autonomous Vehicle Technical Committee and Vice Chair of the IEEE Autonomous Driving Standards Working Group. Dr. Yang has published more than 100 papers and more than 20 Chinese and American patents, and won the ACM SIGSOFT Outstanding Paper Award and ACM TODAES Best Journal Paper Award.",
      "role": "Professor",
      "org": "University of Science and Technology of China",
      "roleOrg": "Professor at University of Science and Technology of China",
      "image": "james-yang.png",
      "tag": "embodied-ai",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "paul-yang",
      "name": "Paul Yang",
      "bio": "At Runhouse, Paul is helping to build, test, and deploy Kubetorch, spending most of his time recently on product discovery and partner engineering for scaled ML use cases as Kubetorch prepares for public launch. Previously, he worked across a range of ML/DS domain areas, from language model tuning and evaluations for contextually aware code generation to productizing causal ML / pseudo-causal inference. ",
      "role": "ML Engineering",
      "org": "Runhouse",
      "roleOrg": "ML Engineering at Runhouse",
      "image": "paul-yang.jpeg",
      "tag": "ai-infra",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "eitan-yarmush",
      "name": "Eitan Yarmush",
      "bio": "I am a software engineer currently working at Solo.io In Boston Massachusetts. I am a skilled problem solver, communicator, and mentor. My current passion and focus is reimagining AI in the Open Source, and how that can help enterprises succeed.",
      "role": "Senior Architect",
      "org": "solo.io",
      "roleOrg": "Senior Architect at solo.io",
      "image": "eitan-yarmush.jpg",
      "tag": "ai-apps",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "https://github.com/EItanya",
        "linkedin": "https://www.linkedin.com/in/eitan-yarmush-82890595/",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "min-zhang",
      "tag": "embodied-ai",
      "name": "Min Zhang",
      "roleOrg": "EU Director of Unitree Robotics",
      "bio": "Min Zhang, EU Director of Unitree Robotics\r\n\r\nUnitree Robotics is a world-renowned civilian robotics company, which is focusing on the R&D, production, and sales of consumer and industry-class high-performance general-purpose legged and humanoid robots, six-axis manipulators, and so on. Unitree Robotics has been invited to attend the 2021 CCTV Spring Festival Gala, the opening ceremony of Winter Olympic 2022, the 2023 Super Bowl, The 19th Asian Games and The 4th Asian Para Games, and has been interviewed and reported by CCTV, BBC and other well-known media for many times. Unitree Robotics is the world's first company to start public retail of high-performance quadruped robots, and the first to achieve industry landing, with global sales leading over the years.\r\nUnitree has excellent leadership in core robot parts, motion control, robot sensing and other comprehensive fields\r\nUnitree attaches great importance to independent research and development and technological innovation, fully self-researching key core robot components such as motors, reducers, controllers, LIDAR and high-performance perception and motion control algorithms, integrating the entire robotics industry chain, and reaching global technological leadership in the field of quadruped robots. At present, we have applied for more than 180 domestic patents and granted more than 150 patents all over the world.",
      "image": "min-zhang.png",
      "org": "Unitree Robotics",
      "role": "EU Director ",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://twitter.com/UnitreeRobotics",
        "github": "https://github.com/unitreerobotics",
        "linkedin": "https://www.linkedin.com/company/unitreerobotics",
        "website": "https://www.unitree.com/en/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "yingfeng-zhang",
      "tag": "ai-apps",
      "name": "Yingfeng Zhang",
      "roleOrg": "CEO of InfiniFlow",
      "bio": "Co-founder of InfinFlow and a seasoned entrepreneur, has for years spearheaded Infrastructure R&D across search engines, database engines, cloud infrastructure, and big data architecture. With extensive AI expertise in advertising, recommender systems, and computer vision (notably developing InsightFace, a top facial recognition algorithm), he has successfully led the digital transformation of multiple large enterprises and robustly supported internet services boasting over 10 million daily active users and 200 million daily dynamic search requests.\r\n\r\n英飞流联合创始人，连续创业者，先后负责多年Infrastructure研发，涵盖搜索引擎，数据库内核，云计算基础架构和大数据架构等，从事多年人工智能核心算法研发，包括广告、推荐引擎和计算机视觉。先后主导并参与多家大型企业数字化转型，支撑过日活千万，日均两亿搜索动态请求的互联网业务",
      "image": "yingfeng-zhang.png",
      "org": "InfiniFlow",
      "role": "CEO",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "https://x.com/infiniflowai",
        "github": "https://github.com/infiniflow",
        "linkedin": "https://www.linkedin.com/company/infiniflow/",
        "website": "https://ragflow.io/"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "junkai-zhao",
      "name": "Junkai Zhao",
      "bio": "I am a Robotics Algorithm Engineer at the Beijing Academy of Artificial Intelligence, where I focus on developing general-purpose robotic manipulation models. Prior to this, I worked at Agibot and the Shanghai Qizhi Institute, contributing to projects involving motion planning, control systems, and long-horizon robotic manipulation. My expertise spans robot control, simulation environments, and learning-based action modeling.",
      "role": "Robot Algorithm Engineer",
      "org": "BAAI",
      "roleOrg": "Robot Algorithm Engineer at BAAI",
      "image": "junkai-zhao.jpg",
      "tag": "embodied-ai",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "yaowei-zheng",
      "tag": "ai-infra",
      "name": "Yaowei Zheng",
      "roleOrg": "Ph.D. Student at Beihang University",
      "bio": "Yaowei Zheng is currently a 4-th year Ph.D. student at Beihang University. He is the founder of LLaMA Factory, one of the most popular libraries for fine-tuning LLMs. As the first author, he has published several conference papers in ACL, CVPR, and WWW. He serves as a reviewer for AAAI and EMNLP. He was awarded the Outstanding Open-Source Contributor for the Ascend Ecosystem. He has been invited to deliver keynote speech at GOSIM China 2024.",
      "image": "yaowei-zheng.jpeg",
      "org": "Beihang University",
      "role": "Ph.D. Student",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "https://scholar.google.com/citations?user=QQtacXUAAAAJ"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "yiran-zhong",
      "tag": "ai-model",
      "name": "Yiran Zhong",
      "roleOrg": "Senior Research Director at MiniMax",
      "bio": "Dr. Yiran Zhong is the Senior Research Director at MiniMax, where he leads the design of large model network architectures and the development of multimodal deep reasoning models. Previously, he served as a Young Scientist at the Shanghai Artificial Intelligence Laboratory, heading the New Architecture Exploration Group as the Principal Investigator (PI).\r\n\r\nDr. Zhong earned his Ph.D. from the Australian National University, under the guidance of Professor Hongdong Li and Professor Richard Hartley, a Fellow of the Royal Society. He has authored over 20 papers in leading international conferences and journals, advancing non-Transformer architectures such as Linear Attention Mechanisms, Long Convolutions, and Linear Recurrent Networks (Linear RNN).",
      "image": "yiran-zhong.png",
      "org": "MiniMax",
      "role": "Senior Research Director",
      "socialLinks": {
        "mastodon": "undefined",
        "twitter": "undefined",
        "github": "undefined",
        "linkedin": "undefined",
        "website": "undefined"
      },
      "status": "New",
      "draft": False
    },
    {
      "id": "tbd",
      "tag": "ai-apps",
      "name": "Speaker to be Announced",
      "roleOrg": "",
      "bio": "Speaker to be announced soon",
      "image": "generic-profile.png",
      "org": ""
    }
  ]
    all_name = read_json_lines(new_json_file)
    for speaker in all_speakers:
        if speaker['name'] not in all_name:
          user_input =json.dumps(str(speaker))
          response = client.chat.completions.create(
          model="gpt-4o-mini",
          messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content":user_input},
          ],
          )
          result = response.choices[0].message
          speaker['pedia'] = result.content
          print(result.content)
          append_data_to_txt(file_path=new_json_file, new_data=speaker)

