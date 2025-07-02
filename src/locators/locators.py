from selenium.webdriver.common.by import By

class EnterLocators:
    # вход по кнопке «Войти в аккаунт» на главной
    ENTER_MAIN = By.XPATH, "//button[contains(@class,'button_button__33qZ0')]"
    # поле Имя на странице registration
    NAME_FIELD = By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(text(), 'Имя')]/following::input[1]"
    # поле Email на странице login и registration
    EMAIL_FIELD = By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(text(), 'Email')]/following::input[1]"
    # поле Пароль на странице login и registration
    PASSWORD_FIELD = By.XPATH, "//label[contains(@class, 'input__placeholder') and contains(text(), 'Пароль')]/following::input[1]"
    # кнопка сделать заказ
    ORDER_BUTTON = By.XPATH, "//button[contains(@class,'button_button__33qZ0')]"
    # ссылка на личный кабинет в хидере
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX' ) and @href='/account']"
    # кнопка Войти на странице регистрации и восстановления пароля
    LOG_IN_BUTTON_REGISTRATION_AND_RECOVERY_FORM = By.XPATH,"//a[@class = 'Auth_link__1fOlj']"
    # ошибка некорректный пароль
    INCORRECT_PASSWORD = By.XPATH, "//form//div[contains(@class, 'input_status_error')]"
    # ссылка на конструктор в хидере
    CONSTRUCTOR_HEADER = By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va' ) and text()='Конструктор']"
    # ссылка на логотип стеллар бургер в хидере
    STELLAR_BURGER_HEADER = By.XPATH,  "//div[@class='AppHeader_header__logo__2D0X2']"
    # кнопка выход в личном кабинете
    EXIT_BUTTON_IN_PERSONAL_CABINET = By.XPATH, "//button[contains(@class,'Account_button__14Yp3')]"
    # вкладка Булки в конструкторе
    BREADS_TAB = By.XPATH, "//span[text()='Булки']"
    # активная вкладка Булки в конструкторе
    CURRENT_BREADS_TAB = By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')] //span[text()='Булки']"
    # вкладка Соусы в конструкторе
    SAUCES_TAB = By.XPATH, "//span[text()='Соусы']"
    # активная вкладка Соусы в конструкторе
    CURRENT_SAUCES_TAB = By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')] //span[text()='Соусы']"
    # вкладка Начинки в конструкторе
    TOPPINGS_TAB = By.XPATH, "//span[text()='Начинки']"
    # активная вкладка Начинки в конструкторе
    CURRENT_TOPPINGS_TAB = By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')] //span[text()='Начинки']"