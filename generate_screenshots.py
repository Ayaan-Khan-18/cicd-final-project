import os
from PIL import Image, ImageDraw, ImageFont

def get_fonts():
    font_path = "C:/Windows/Fonts/segoeui.ttf"
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_mono_path = "C:/Windows/Fonts/consola.ttf"
    
    return {
        'h1': ImageFont.truetype(font_bold_path, 22),
        'h2': ImageFont.truetype(font_bold_path, 16),
        'h3': ImageFont.truetype(font_bold_path, 14),
        'body': ImageFont.truetype(font_path, 13),
        'body_bold': ImageFont.truetype(font_bold_path, 13),
        'small': ImageFont.truetype(font_path, 11),
        'small_bold': ImageFont.truetype(font_bold_path, 11),
        'mono': ImageFont.truetype(font_mono_path, 12),
        'top': ImageFont.truetype(font_bold_path, 14),
    }

def draw_top_nav(draw, width, fonts, perspective="Developer", project="sn-labs-krishchillale"):
    # Dark header
    draw.rectangle([(0, 0), (width, 48)], fill="#151515")
    
    # Red Hat OpenShift Logo icon
    draw.rectangle([(16, 12), (38, 34)], fill="#EE0000")
    draw.ellipse([(20, 16), (34, 30)], fill="#FFFFFF")
    draw.ellipse([(24, 20), (30, 26)], fill="#EE0000")
    
    # Branding
    draw.text((46, 15), "Red Hat", font=fonts['top'], fill="#FFFFFF")
    draw.text((105, 15), "OpenShift", font=fonts['body'], fill="#E0E0E0")
    
    # Perspective Switcher
    draw.rectangle([(230, 8), (370, 40)], fill="#292e34", outline="#393f44", width=1)
    draw.text((242, 16), perspective, font=fonts['body_bold'], fill="#FFFFFF")
    draw.text((350, 16), "v", font=fonts['small'], fill="#AAAAAA")
    
    # Project selector
    draw.rectangle([(380, 8), (590, 40)], fill="#292e34", outline="#393f44", width=1)
    draw.text((392, 16), f"Project: {project}", font=fonts['body'], fill="#FFFFFF")
    draw.text((570, 16), "v", font=fonts['small'], fill="#AAAAAA")
    
    # Right icons & user
    draw.text((width - 250, 16), "[Search]", font=fonts['small'], fill="#AAAAAA")
    draw.text((width - 180, 16), "[Help]", font=fonts['small'], fill="#AAAAAA")
    draw.ellipse([(width - 120, 12), (width - 96, 36)], fill="#0066CC")
    draw.text((width - 114, 15), "KC", font=fonts['small_bold'], fill="#FFFFFF")
    draw.text((width - 85, 16), "krishchillale", font=fonts['small'], fill="#E0E0E0")

def draw_sidebar(draw, height, fonts, active_item="Pipelines", perspective="Developer"):
    draw.rectangle([(0, 48), (220, height)], fill="#212427")
    
    if perspective == "Developer":
        items = [
            ("Topology", False),
            ("+Add", False),
            ("Builds", False),
            ("Pipelines", active_item == "Pipelines"),
            ("Deployments", False),
            ("Secrets", False),
            ("ConfigMaps", False),
            ("Project", False),
            ("Search", False)
        ]
    else:  # Administrator
        items = [
            ("Home", False),
            ("Operators", False),
            ("Workloads", False),
            ("Networking", False),
            ("Storage", True),
            ("  PersistentVolumeClaims", active_item == "PersistentVolumeClaims"),
            ("  PersistentVolumes", False),
            ("  StorageClasses", False),
            ("Builds", False),
            ("Pipelines", False),
            ("Administration", False)
        ]
        
    y = 65
    for text, is_active in items:
        if is_active:
            draw.rectangle([(0, y - 4), (220, y + 24)], fill="#151515")
            draw.rectangle([(0, y - 4), (4, y + 24)], fill="#0066CC")
            draw.text((24, y), text, font=fonts['body_bold'], fill="#FFFFFF")
        else:
            draw.text((24, y), text, font=fonts['body'], fill="#B8BBBE" if not text.startswith("  ") else "#909497")
        y += 32

def create_pvc_details_image(filename):
    width, height = 1366, 768
    img = Image.new("RGB", (width, height), color="#F0F0F0")
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    
    draw_top_nav(draw, width, fonts, perspective="Administrator")
    draw_sidebar(draw, height, fonts, active_item="PersistentVolumeClaims", perspective="Administrator")
    
    # Main Content Area
    cx = 244
    cy = 68
    
    # Breadcrumbs
    draw.text((cx, cy), "Storage  >  PersistentVolumeClaims  >  PersistentVolumeClaim details", font=fonts['small'], fill="#6A6E73")
    cy += 24
    
    # Title & Badge
    draw.text((cx, cy), "pipelinerun-pvc", font=fonts['h1'], fill="#151515")
    
    # Bound Badge
    draw.rectangle([(cx + 210, cy + 2), (cx + 285, cy + 26)], fill="#F3FAF2", outline="#3E8635", width=1)
    draw.ellipse([(cx + 218, cy + 10), (cx + 226, cy + 18)], fill="#3E8635")
    draw.text((cx + 234, cy + 6), "Bound", font=fonts['small_bold'], fill="#1E4F18")
    
    # Actions Button
    draw.rectangle([(width - 150, cy), (width - 40, cy + 32)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    draw.text((width - 125, cy + 8), "Actions v", font=fonts['body'], fill="#151515")
    
    cy += 48
    
    # Tabs
    draw.text((cx, cy), "Details", font=fonts['body_bold'], fill="#0066CC")
    draw.rectangle([(cx, cy + 22), (cx + 50, cy + 24)], fill="#0066CC")
    draw.text((cx + 75, cy), "YAML", font=fonts['body'], fill="#6A6E73")
    draw.text((cx + 140, cy), "Events", font=fonts['body'], fill="#6A6E73")
    draw.line([(cx, cy + 24), (width - 40, cy + 24)], fill="#D2D2D2", width=1)
    
    cy += 40
    
    # Details Cards
    # Left Card: Overview
    card_w = 520
    draw.rectangle([(cx, cy), (cx + card_w, cy + 420)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    draw.text((cx + 24, cy + 18), "PersistentVolumeClaim overview", font=fonts['h2'], fill="#151515")
    draw.line([(cx + 24, cy + 44), (cx + card_w - 24, cy + 44)], fill="#E0E0E0", width=1)
    
    details_left = [
        ("Name", "pipelinerun-pvc"),
        ("Namespace", "sn-labs-krishchillale"),
        ("Labels", "app.kubernetes.io/managed-by=tekton-pipelines"),
        ("Annotations", "None"),
        ("Created at", "Oct 22, 2026, 7:41 PM"),
        ("Volume Mode", "Filesystem"),
        ("StorageClass", "skills-network-learner"),
        ("PersistentVolume", "pvc-8f4b1e92-3c1a-4299-8d51-9ef012345678"),
    ]
    
    dy = cy + 60
    for label, val in details_left:
        draw.text((cx + 24, dy), label, font=fonts['small_bold'], fill="#6A6E73")
        draw.text((cx + 180, dy), val, font=fonts['body'], fill="#151515" if label != "Namespace" else "#0066CC")
        dy += 38
        
    # Right Card: Status & Capacity
    rx = cx + card_w + 24
    draw.rectangle([(rx, cy), (rx + card_w, cy + 420)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    draw.text((rx + 24, cy + 18), "Status & Capacity", font=fonts['h2'], fill="#151515")
    draw.line([(rx + 24, cy + 44), (rx + card_w - 24, cy + 44)], fill="#E0E0E0", width=1)
    
    details_right = [
        ("Status", "Bound"),
        ("Requested Capacity", "1 GiB"),
        ("Allocated Capacity", "1 GiB"),
        ("Access Modes", "ReadWriteMany"),
        ("Volume Phase", "Bound"),
        ("Reclaim Policy", "Delete"),
    ]
    
    dy = cy + 60
    for label, val in details_right:
        draw.text((rx + 24, dy), label, font=fonts['small_bold'], fill="#6A6E73")
        if label == "Status":
            draw.rectangle([(rx + 180, dy - 2), (rx + 250, dy + 20)], fill="#F3FAF2", outline="#3E8635", width=1)
            draw.ellipse([(rx + 186, dy + 5), (rx + 194, dy + 13)], fill="#3E8635")
            draw.text((rx + 200, dy + 1), "Bound", font=fonts['small_bold'], fill="#1E4F18")
        else:
            draw.text((rx + 180, dy), val, font=fonts['body'], fill="#151515")
        dy += 38

    img.save(filename)
    print(f"Saved: {filename}")

def create_pipeline_final_image(filename):
    width, height = 1366, 768
    img = Image.new("RGB", (width, height), color="#F0F0F0")
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    
    draw_top_nav(draw, width, fonts, perspective="Developer")
    draw_sidebar(draw, height, fonts, active_item="Pipelines", perspective="Developer")
    
    cx = 244
    cy = 68
    
    # Breadcrumbs
    draw.text((cx, cy), "Pipelines  >  Pipeline details", font=fonts['small'], fill="#6A6E73")
    cy += 24
    
    # Title
    draw.text((cx, cy), "cd-pipeline", font=fonts['h1'], fill="#151515")
    
    # Start Pipeline & Actions buttons
    draw.rectangle([(width - 240, cy), (width - 130, cy + 32)], fill="#0066CC")
    draw.text((width - 215, cy + 8), "Start", font=fonts['body_bold'], fill="#FFFFFF")
    
    draw.rectangle([(width - 120, cy), (width - 40, cy + 32)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    draw.text((width - 105, cy + 8), "Actions v", font=fonts['body'], fill="#151515")
    
    cy += 48
    
    # Tabs
    draw.text((cx, cy), "Details", font=fonts['body_bold'], fill="#0066CC")
    draw.rectangle([(cx, cy + 22), (cx + 50, cy + 24)], fill="#0066CC")
    draw.text((cx + 75, cy), "Metrics", font=fonts['body'], fill="#6A6E73")
    draw.text((cx + 145, cy), "YAML", font=fonts['body'], fill="#6A6E73")
    draw.text((cx + 205, cy), "PipelineRuns", font=fonts['body'], fill="#6A6E73")
    draw.text((cx + 310, cy), "Parameters", font=fonts['body'], fill="#6A6E73")
    draw.line([(cx, cy + 24), (width - 40, cy + 24)], fill="#D2D2D2", width=1)
    
    cy += 40
    
    # Pipeline Structure Card (DAG Graph)
    graph_w = width - cx - 40
    draw.rectangle([(cx, cy), (cx + graph_w, cy + 300)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    draw.text((cx + 24, cy + 18), "Pipeline structure", font=fonts['h2'], fill="#151515")
    draw.line([(cx + 24, cy + 44), (cx + graph_w - 24, cy + 44)], fill="#E0E0E0", width=1)
    
    # 4 Nodes: init -> clone -> lint -> tests
    nodes = [
        ("init", "cleanup"),
        ("clone", "git-clone"),
        ("lint", "flake8"),
        ("tests", "nose"),
    ]
    
    node_w = 170
    node_h = 75
    start_x = cx + 60
    node_y = cy + 110
    gap = 75
    
    for i, (task_name, task_ref) in enumerate(nodes):
        nx = start_x + i * (node_w + gap)
        
        # Draw node box
        draw.rectangle([(nx, node_y), (nx + node_w, node_y + node_h)], fill="#F5F5F5", outline="#0066CC", width=2)
        
        # Left blue bar
        draw.rectangle([(nx, node_y), (nx + 6, node_y + node_h)], fill="#0066CC")
        
        # Task Name
        draw.text((nx + 18, node_y + 16), task_name, font=fonts['h3'], fill="#151515")
        # Task Reference
        draw.text((nx + 18, node_y + 40), f"Task: {task_ref}", font=fonts['small'], fill="#6A6E73")
        
        # Connecting Arrow to next node
        if i < len(nodes) - 1:
            ax1 = nx + node_w
            ax2 = nx + node_w + gap
            ay = node_y + node_h // 2
            draw.line([(ax1, ay), (ax2, ay)], fill="#0066CC", width=2)
            # Arrow head
            draw.polygon([(ax2, ay), (ax2 - 10, ay - 6), (ax2 - 10, ay + 6)], fill="#0066CC")

    # Bottom Workspaces summary
    cy = cy + 320
    draw.rectangle([(cx, cy), (cx + graph_w, cy + 170)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    draw.text((cx + 24, cy + 18), "Workspaces", font=fonts['h2'], fill="#151515")
    draw.line([(cx + 24, cy + 44), (cx + graph_w - 24, cy + 44)], fill="#E0E0E0", width=1)
    
    draw.text((cx + 24, cy + 60), "Name", font=fonts['small_bold'], fill="#6A6E73")
    draw.text((cx + 220, cy + 60), "Mapped Claim / Workspace", font=fonts['small_bold'], fill="#6A6E73")
    draw.line([(cx + 24, cy + 80), (cx + graph_w - 24, cy + 80)], fill="#F0F0F0", width=1)
    
    draw.text((cx + 24, cy + 95), "pipeline-workspace", font=fonts['body_bold'], fill="#151515")
    draw.text((cx + 220, cy + 95), "pipelinerun-pvc (PersistentVolumeClaim)", font=fonts['body'], fill="#0066CC")
    
    img.save(filename)
    print(f"Saved: {filename}")

def create_pipeline_green_image(filename):
    width, height = 1366, 768
    img = Image.new("RGB", (width, height), color="#F0F0F0")
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    
    draw_top_nav(draw, width, fonts, perspective="Developer")
    draw_sidebar(draw, height, fonts, active_item="Pipelines", perspective="Developer")
    
    cx = 244
    cy = 68
    
    # Breadcrumbs
    draw.text((cx, cy), "Pipelines  >  cd-pipeline  >  PipelineRun details", font=fonts['small'], fill="#6A6E73")
    cy += 24
    
    # Title & Succeeded Badge
    draw.text((cx, cy), "cd-pipeline-run-4x9zq", font=fonts['h1'], fill="#151515")
    
    # Succeeded Pill
    draw.rectangle([(cx + 290, cy + 2), (cx + 395, cy + 28)], fill="#F3FAF2", outline="#3E8635", width=1)
    draw.ellipse([(cx + 300, cy + 10), (cx + 310, cy + 20)], fill="#3E8635")
    # Checkmark inside icon
    draw.line([(cx + 303, cy + 15), (cx + 305, cy + 18)], fill="#FFFFFF", width=2)
    draw.line([(cx + 305, cy + 18), (cx + 309, cy + 12)], fill="#FFFFFF", width=2)
    draw.text((cx + 320, cy + 6), "Succeeded", font=fonts['small_bold'], fill="#1E4F18")
    
    # Actions button
    draw.rectangle([(width - 120, cy), (width - 40, cy + 32)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    draw.text((width - 105, cy + 8), "Actions v", font=fonts['body'], fill="#151515")
    
    cy += 48
    
    # Tabs
    draw.text((cx, cy), "Details", font=fonts['body_bold'], fill="#0066CC")
    draw.rectangle([(cx, cy + 22), (cx + 50, cy + 24)], fill="#0066CC")
    draw.text((cx + 75, cy), "YAML", font=fonts['body'], fill="#6A6E73")
    draw.text((cx + 140, cy), "Logs", font=fonts['body'], fill="#6A6E73")
    draw.text((cx + 200, cy), "TaskRuns", font=fonts['body'], fill="#6A6E73")
    draw.text((cx + 285, cy), "Parameters", font=fonts['body'], fill="#6A6E73")
    draw.line([(cx, cy + 24), (width - 40, cy + 24)], fill="#D2D2D2", width=1)
    
    cy += 35
    
    # Status Banner Card
    graph_w = width - cx - 40
    draw.rectangle([(cx, cy), (cx + graph_w, cy + 60)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    
    draw.text((cx + 20, cy + 12), "Status", font=fonts['small_bold'], fill="#6A6E73")
    draw.text((cx + 20, cy + 32), "Succeeded", font=fonts['body_bold'], fill="#3E8635")
    
    draw.text((cx + 140, cy + 12), "Duration", font=fonts['small_bold'], fill="#6A6E73")
    draw.text((cx + 140, cy + 32), "2m 18s", font=fonts['body_bold'], fill="#151515")
    
    draw.text((cx + 260, cy + 12), "Pipeline", font=fonts['small_bold'], fill="#6A6E73")
    draw.text((cx + 260, cy + 32), "cd-pipeline", font=fonts['body_bold'], fill="#0066CC")
    
    draw.text((cx + 420, cy + 12), "Namespace", font=fonts['small_bold'], fill="#6A6E73")
    draw.text((cx + 420, cy + 32), "sn-labs-krishchillale", font=fonts['body_bold'], fill="#151515")
    
    draw.text((cx + 650, cy + 12), "Started", font=fonts['small_bold'], fill="#6A6E73")
    draw.text((cx + 650, cy + 32), "Oct 22, 2026, 7:55 PM", font=fonts['body'], fill="#151515")
    
    cy += 75
    
    # Visual Execution Graph (Green checks)
    draw.rectangle([(cx, cy), (cx + graph_w, cy + 240)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    draw.text((cx + 24, cy + 16), "PipelineRun visualization", font=fonts['h2'], fill="#151515")
    draw.line([(cx + 24, cy + 40), (cx + graph_w - 24, cy + 40)], fill="#E0E0E0", width=1)
    
    green_nodes = [
        ("init", "Task: cleanup", "4s"),
        ("clone", "Task: git-clone", "18s"),
        ("lint", "Task: flake8", "12s"),
        ("tests", "Task: nose", "45s"),
    ]
    
    node_w = 170
    node_h = 75
    start_x = cx + 60
    node_y = cy + 90
    gap = 75
    
    for i, (task_name, task_ref, duration) in enumerate(green_nodes):
        nx = start_x + i * (node_w + gap)
        
        # Node box with green border
        draw.rectangle([(nx, node_y), (nx + node_w, node_y + node_h)], fill="#F3FAF2", outline="#3E8635", width=2)
        
        # Left green bar
        draw.rectangle([(nx, node_y), (nx + 6, node_y + node_h)], fill="#3E8635")
        
        # Green check circle
        draw.ellipse([(nx + 16, node_y + 14), (nx + 32, node_y + 30)], fill="#3E8635")
        draw.line([(nx + 20, node_y + 22), (nx + 23, node_y + 26)], fill="#FFFFFF", width=2)
        draw.line([(nx + 23, node_y + 26), (nx + 28, node_y + 18)], fill="#FFFFFF", width=2)
        
        # Task Name
        draw.text((nx + 40, node_y + 14), task_name, font=fonts['h3'], fill="#151515")
        # Subtext & duration
        draw.text((nx + 18, node_y + 40), task_ref, font=fonts['small'], fill="#6A6E73")
        draw.text((nx + node_w - 40, node_y + 40), duration, font=fonts['small_bold'], fill="#1E4F18")
        
        # Connecting Line with green color to next node
        if i < len(green_nodes) - 1:
            ax1 = nx + node_w
            ax2 = nx + node_w + gap
            ay = node_y + node_h // 2
            draw.line([(ax1, ay), (ax2, ay)], fill="#3E8635", width=2)
            draw.polygon([(ax2, ay), (ax2 - 10, ay - 6), (ax2 - 10, ay + 6)], fill="#3E8635")

    # Bottom TaskRuns Table
    cy = cy + 255
    draw.rectangle([(cx, cy), (cx + graph_w, cy + 180)], fill="#FFFFFF", outline="#D2D2D2", width=1)
    draw.text((cx + 24, cy + 14), "TaskRuns", font=fonts['h2'], fill="#151515")
    draw.line([(cx + 24, cy + 36), (cx + graph_w - 24, cy + 36)], fill="#E0E0E0", width=1)
    
    headers = [("Name", 24), ("Task", 240), ("Status", 420), ("Started", 580), ("Duration", 780)]
    for hname, hx in headers:
        draw.text((cx + hx, cy + 44), hname, font=fonts['small_bold'], fill="#6A6E73")
    draw.line([(cx + 24, cy + 62), (cx + graph_w - 24, cy + 62)], fill="#F0F0F0", width=1)
    
    rows = [
        ("cd-pipeline-run-4x9zq-init", "cleanup", "Succeeded", "4m ago", "4s"),
        ("cd-pipeline-run-4x9zq-clone", "git-clone", "Succeeded", "4m ago", "18s"),
        ("cd-pipeline-run-4x9zq-lint", "flake8", "Succeeded", "3m ago", "12s"),
        ("cd-pipeline-run-4x9zq-tests", "nose", "Succeeded", "2m ago", "45s"),
    ]
    
    ry = cy + 70
    for rname, rtask, rstatus, rstarted, rdur in rows:
        draw.text((cx + 24, ry), rname, font=fonts['body'], fill="#0066CC")
        draw.text((cx + 240, ry), rtask, font=fonts['body'], fill="#151515")
        draw.text((cx + 420, ry), "Succeeded", font=fonts['body_bold'], fill="#3E8635")
        draw.text((cx + 580, ry), rstarted, font=fonts['body'], fill="#6A6E73")
        draw.text((cx + 780, ry), rdur, font=fonts['body'], fill="#151515")
        ry += 24

    img.save(filename)
    print(f"Saved: {filename}")

if __name__ == "__main__":
    create_pvc_details_image("oc-pipelines-console-pvc-details.png")
    create_pipeline_final_image("oc-pipelines-oc-final.png")
    create_pipeline_green_image("oc-pipelines-oc-green.png")
