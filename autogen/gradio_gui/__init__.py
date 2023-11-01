def install_dependencies():
    # <------------------- install dependencies  ------------------->
    def try_install_deps(deps, reload_m=[]):
        """
        install dependencies if not installed.
        """
        input(f'You are about to install dependencies {str(deps)}, press Enter to continue ...')
        import subprocess, sys, importlib
        for dep in deps:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', dep])
        import site
        importlib.reload(site)
        for m in reload_m:
            importlib.reload(__import__(m))

    # <-------------------  dependencies  ------------------->
    try:
        import gradio as gr
        import void_terminal
    except:
        try_install_deps(deps=["void-terminal>=0.0.9"]) 
        try_install_deps(deps=["https://github.com/binary-husky/gpt_academic/raw/master/docs/gradio-3.32.6-py3-none-any.whl"])

    if gr.__version__ not in ['3.32.6']: 
        # this is a special version of gradio, which is not available on pypi.org
        try_install_deps(deps=["https://github.com/binary-husky/gpt_academic/raw/master/docs/gradio-3.32.6-py3-none-any.whl"])

def init_config_list():
    import os
    from autogen import config_list_from_json
    config_file_path = os.environ.get("OAI_CONFIG_LIST")
    if config_file_path is None:
        raise EnvironmentError("""
OAI_CONFIG_LIST path is not set.
Please run with 
    `export OAI_CONFIG_LIST='/path/to/OAI_CONFIG_LIST'`
to set the path to config list file, and then run 
    `python -m autogen.launch_gui`
to start the GUI.
""")
    config_list = config_list_from_json(env_or_file=config_file_path)
    llm_config = {"config_list": config_list}
    return llm_config


def init_config():
    import void_terminal
    
    llm_config = init_config_list()
    # set network proxy
    # void_terminal.set_conf(key="USE_PROXY", value=True)
    # void_terminal.set_conf(key="proxies", value='{"http": "http://localhost:10881", "https": "http://localhost:10881"}')
    void_terminal.set_conf(key="AUTOGEN_USE_DOCKER", value=False)
    void_terminal.set_conf(key="PATH_LOGGING", value="gpt_log")
    void_terminal.set_conf(key="DARK_MODE", value=True)
    void_terminal.set_conf(key="AUTO_CLEAR_TXT", value=True)

    # the following configurations only influence direct chat, not autogen
    void_terminal.set_conf(key="API_KEY", value=llm_config["config_list"][0]["api_key"])
    void_terminal.set_conf(key="LLM_MODEL", value=llm_config["config_list"][0]["model"])
    # void_terminal.set_conf(key="API_KEY",value="sk-yourapikey")
    # void_terminal.set_conf(key="LLM_MODEL", value="gpt-3.5-turbo-16k")
    if llm_config["config_list"][0].get('api_type', '') == 'azure':
        model = 'azure-'+llm_config["config_list"][0]["model"]
        api_base = llm_config["config_list"][0]["api_base"]
        if api_base.endswith('/'): api_base = api_base[:-1]
        AZURE_CFG_ARRAY = {
            model:
                {
                    "AZURE_ENDPOINT": llm_config["config_list"][0]["api_base"] + '/',
                    "AZURE_API_KEY": llm_config["config_list"][0]["api_key"],
                    "AZURE_ENGINE": llm_config["config_list"][0]["deployment_id"],
                    "AZURE_MODEL_MAX_TOKEN": 8192,
                },
        }
        void_terminal.set_conf(key="LLM_MODEL", value=model)
        void_terminal.set_conf(key="AZURE_CFG_ARRAY", value=str(AZURE_CFG_ARRAY))
    return llm_config