import json
import streamlit as st

def init():
    hide_streamlit_style = """
    <style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
def logo():
    sidebar_logo = "./image/icon_red.png"
    main_body_logo = "./image/icon_blue.png"
    st.logo(sidebar_logo, icon_image=main_body_logo)

st.set_page_config(
    page_title='Машинное обучение без программирования: Sechenov.AutoML',
    initial_sidebar_state="expanded"
)
init()
logo()
html_style_string = '''<style>
@media (min-width: 576px)
section div.block-container {
  padding-left: 20rem;
}
section div.block-container {
  padding-left: 4rem;
  padding-right: 4rem;
  max-width: 80rem;
}  
.floating-side-bar {
    display: flex;
    flex-direction: column;
    position: fixed;
    margin-top: 2rem;
    margin-left: 2.75rem;
    margin-right: 2.75rem;
}
.flt-bar-hd {
    color: #5e6572;
    margin: 1rem 0.1rem 0 0;
}
.floating-side-bar a {
    color: #b3b8c2;

}
.floating-side-bar a:hover {

}
.floating-side-bar a.l2 {

}
</style>'''

st.markdown(html_style_string, unsafe_allow_html=True)
col1, col2 = st.columns([6,2])
with col1:
    st.markdown("## О курсе")
    st.markdown("Курс **Машинное обучение в здравоохранении** - это образовательная программа, которая фокусируется на применении методов машинного обучения в области здравоохранения.")
    st.markdown("### Темы курса")
    st.markdown("Этот курс охватывать следующие темы:")
    st.markdown("- **Введение в машинное обучение:** Основные понятия и методы машинного обучения, такие как обучение с учителем и без учителя, регрессия, классификация и кластеризация.")
    st.markdown("- **Применение машинного обучения в здравоохранении:** Использование машинного обучения для анализа медицинских данных, прогнозирования заболеваний, диагностики и лечения.")
    st.markdown("- **Медицинские данные:** Типы медицинских данных, такие как изображения, сигналы и текстовые данные, и способы их обработки и анализа.")
    st.markdown("- **Анализ изображений в медицине:** Использование машинного обучения для анализа медицинских изображений, таких как рентгеновские снимки, КТ и МРТ.")
    st.markdown("- **Прогнозирование заболеваний:** Использование машинного обучения для прогнозирования заболеваний, таких как диабет, рак и сердечно-сосудистые заболевания.")
    st.markdown("- **Диагностика заболеваний:** Использование машинного обучения для диагностики заболеваний, таких как рак, на основе медицинских данных.")
    st.markdown("- **Лечение заболеваний:** Использование машинного обучения для разработки персонализированных планов лечения заболеваний.")
    st.markdown("- **Этические и юридические аспекты:** Этические и юридические аспекты использования машинного обучения в здравоохранении, такие как конфиденциальность данных и ответственность за ошибки.")
    st.markdown("- **Примеры применения:** Примеры применения машинного обучения в различных областях здравоохранения, таких как кардиология, онкология и неврология.")
    st.markdown("Целью этого курса является предоставление студентам знаний и навыков, необходимых для применения машинного обучения в здравоохранении, а также для понимания этических и юридических аспектов использования машинного обучения в этой области.")
    st.markdown("### Слушатели курса")
    st.markdown("Курс рассчитан на различные категории слушателей, включая:")
    st.markdown("- **Студентов** медицинских вузов для получения навыков обработки медицинских данных, построения моделей машинного обучения для задач диагностики (классификация) и предиктивной аналитики (прогнозирования) на основе медицинских данных и датасетов")
    st.markdown("- **Специалистов здравоохранения**, интересующихся машинным обучением")
    st.markdown("- **Разработчиков программного обеспечения**, работающих в области здравоохранения")
    st.markdown("- **Исследователей**, занимающихся разработкой новых методов машинного обучения в здравоохранении.")

    st.code("python -m pip install streamlit_code_editor")
    st.markdown("replacing `python` with the correct version of python for your setup (e.g. `python3` or `python3.8`). Or if you are certain the correct version of python will be used to run pip, you can install with just:")
    st.code("pip install streamlit_code_editor")

    st.markdown("#### Схема или рисунок")
    st.markdown("After importing the module, you can .... tring:")
    st.image("pages/resources/1_P/code_editor_layout.png")

    st.markdown("#### Формула в формате LaTex")
    st.markdown("Вставка формул и математических выражений в формате LaTex:")
    st.latex(r'''
            a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
            \sum_{k=0}^{n-1} ar^k =
            a \left(\frac{1-r^{n}}{1-r}\right)
            ''')

    st.markdown("#### Видео-курс")
    st.markdown("After importing the module, you can call the `code_editor` function with just a string:")
    st.markdown("Without specifying a language, the editor will default to `python`. You can also specify a language with the `lang` argument:")
    video_file = open('pages/resources/1_P/mod1_1.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown("The two blocks of code above are displayed in code editors. As the name of the component implies, you can edit the code. Try it out! ")
    st.markdown("By default, each code editor is styled like streamlit's [code block element](https://docs.streamlit.io/library/api-reference/text/st.code). The next sections will go over how to customize the styling of the editor.")



    st.subheader('Разное')
    st.write('''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus. Amet mauris commodo quis imperdiet. In metus vulputate eu scelerisque. Facilisis gravida neque convallis a cras semper. Quis vel eros donec ac odio. Posuere urna nec tincidunt praesent semper feugiat nibh sed. Vitae et leo duis ut. Consectetur lorem donec massa sapien faucibus et molestie ac feugiat. Scelerisque varius morbi enim nunc faucibus a. Eget velit aliquet sagittis id consectetur purus ut. Massa eget egestas purus viverra. Libero justo laoreet sit amet cursus sit. Nibh nisl condimentum id venenatis a condimentum vitae sapien.

    Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. Eget est lorem ipsum dolor sit amet consectetur. Tortor pretium viverra suspendisse potenti. Diam maecenas ultricies mi eget mauris pharetra. Ultrices mi tempus imperdiet nulla. Volutpat ac tincidunt vitae semper quis. Viverra accumsan in nisl nisi scelerisque eu. Ut aliquam purus sit amet luctus venenatis lectus magna fringilla. Velit ut tortor pretium viverra suspendisse potenti nullam ac.

    Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed blandit libero volutpat sed cras. Fringilla est ullamcorper eget nulla. Egestas sed tempus urna et pharetra pharetra massa massa. Nunc vel risus commodo viverra maecenas accumsan lacus. Justo donec enim diam vulputate ut pharetra. Metus aliquam eleifend mi in nulla posuere sollicitudin. Lobortis mattis aliquam faucibus purus. Massa tincidunt dui ut ornare lectus sit amet. Et molestie ac feugiat sed lectus vestibulum. Mattis ullamcorper velit sed ullamcorper. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Pulvinar sapien et ligula ullamcorper malesuada. Orci phasellus egestas tellus rutrum tellus pellentesque. Ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet. Etiam erat velit scelerisque in dictum non consectetur.
    ''')
    st.info('This is a purely informational message', icon="ℹ️")
    st.success("**Tip:** If you set both `minLines` and `maxLines` to the same value, the editor will fix its size to fit only that number of lines of text. This is useful if you want the editor to have a static size and you want to size it according to number of lines to show.")
    st.info("**Note:** The height property does not limit the contents of the editor. Content that exceeds the height will be scrollable.")

    st.header('Модуль-2')
    st.write('''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus. Amet mauris commodo quis imperdiet. In metus vulputate eu scelerisque. Facilisis gravida neque convallis a cras semper. Quis vel eros donec ac odio. Posuere urna nec tincidunt praesent semper feugiat nibh sed. Vitae et leo duis ut. Consectetur lorem donec massa sapien faucibus et molestie ac feugiat. Scelerisque varius morbi enim nunc faucibus a. Eget velit aliquet sagittis id consectetur purus ut. Massa eget egestas purus viverra. Libero justo laoreet sit amet cursus sit. Nibh nisl condimentum id venenatis a condimentum vitae sapien.

    Dictumst vestibulum rhoncus est pellentesque. Egestas sed tempus urna et pharetra pharetra. Eget est lorem ipsum dolor sit amet consectetur. Tortor pretium viverra suspendisse potenti. Diam maecenas ultricies mi eget mauris pharetra. Ultrices mi tempus imperdiet nulla. Volutpat ac tincidunt vitae semper quis. Viverra accumsan in nisl nisi scelerisque eu. Ut aliquam purus sit amet luctus venenatis lectus magna fringilla. Velit ut tortor pretium viverra suspendisse potenti nullam ac.

    Commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Pulvinar mattis nunc sed blandit libero volutpat sed cras. Fringilla est ullamcorper eget nulla. Egestas sed tempus urna et pharetra pharetra massa massa. Nunc vel risus commodo viverra maecenas accumsan lacus. Justo donec enim diam vulputate ut pharetra. Metus aliquam eleifend mi in nulla posuere sollicitudin. Lobortis mattis aliquam faucibus purus. Massa tincidunt dui ut ornare lectus sit amet. Et molestie ac feugiat sed lectus vestibulum. Mattis ullamcorper velit sed ullamcorper. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Pulvinar sapien et ligula ullamcorper malesuada. Orci phasellus egestas tellus rutrum tellus pellentesque. Ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet. Etiam erat velit scelerisque in dictum non consectetur.
    ''')


floating_side_bar = '''
<div class="floating-side-bar">
    <span class="flt-bar-hd"> Содержание </span>
    <a href="#f11e587">О курсе</a>
    <a class="l2" href="#f34a4d15">Темы</a>
    <a class="l2" href="#1cf54309">Слушатели</a>
    <a href="#e3475a88">Видео</a>
    <a href="#1d224f18">Рисунок</a>
    <a href="#3698d889">Формула</a>
    <a href="#343c37c">Разное</a>
    <a href="#4914f6ad">Модули</a>
    <span class="flt-bar-hd"> Ссылки </span>
    <a href="https://ml.datamed.pro/">Sechenov.AutoML</a>
    <a href="https://docs.streamlit.io/library/api-reference/text/st.code">Руководство</a>
</div>
'''

with col2:
    st.markdown(floating_side_bar, unsafe_allow_html=True)



