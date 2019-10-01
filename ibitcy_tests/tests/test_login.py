import allure
import pytest

from hamcrest import equal_to, contains_string
from hamcrest.core import assert_that

from data.users import UsersCredentials
from pages.payment_page import PaymentPage
from utils.driver import Driver
from pages.login_page import LoginPage


class TestAuth:
    @pytest.mark.parametrize(argnames='login,password,lang_btn_loc',
                             argvalues=[
                                 (UsersCredentials.user_01['login'], UsersCredentials.user_01['password'],
                                  LoginPage.en_btn),
                                 (UsersCredentials.user_02['login'], UsersCredentials.user_02['password'],
                                  LoginPage.ch_btn),
                                 (UsersCredentials.user_03['login'], UsersCredentials.user_03['password'],
                                  LoginPage.hi_btn),
                                 (UsersCredentials.user_04['login'], UsersCredentials.user_04['password'],
                                  LoginPage.ko_btn),
                                 (UsersCredentials.user_01['login'], UsersCredentials.user_01['password'],
                                  LoginPage.ru_btn)
                             ])
    def test_success_auth(self, login, password, lang_btn_loc):
        Driver().get_url_with_basic_auth(LoginPage.BASE_URL)
        lang_btn_loc().click()
        LoginPage.login_input().wait_for_displayed().fill(login)
        LoginPage.password_input().fill(password)
        LoginPage.submit_btn().click()
        PaymentPage.status_selector().wait_for_displayed().assert_displayed()
        active_status = PaymentPage.gold_item().text
        with allure.step("Проверяем что активен статус Gold"):
            assert_that(active_status, contains_string('GOLD\n$1000 +100%'))

    @pytest.mark.parametrize(argnames='lang_btn_loc,popup_text,btn_text',
                             argvalues=[
                                 (LoginPage.en_btn, 'New password was send to your email address', 'Close'),
                                 (LoginPage.ch_btn, '새 비밀번호가 이메일로 전송되었습니다.', '关闭'),
                                 (LoginPage.hi_btn, 'आपके मेल पर एक नया पासवर्ड सफलतापूर्वक भेजा गया है।', 'पास'),
                                 (LoginPage.ko_btn, '새 암호가 성공적으로 전자 메일로 보내졌다', '닫기'),
                                 (LoginPage.ru_btn, 'Новый пароль успешно отправлен на Вашу почту', 'Закрыть')
                             ])
    def test_forgot_password(self, lang_btn_loc, popup_text, btn_text):
        Driver().get_url_with_basic_auth(LoginPage.BASE_URL)
        lang_btn_loc().click()
        LoginPage.forgot_pass_btn().click()
        LoginPage.forgot_pass_input().wait_for_displayed().fill('test@test')
        LoginPage.forgot_pass_send_btn().click()
        LoginPage.FailAuthPopUp.notification_popup().wait_for_displayed()
        '''
        Логически правильно было бы вынести это в отдельные тесты на локализацию, 
        но т.к. посути это эмуляция отправки пароля я использовал это и тут
        '''
        popup_existed_text = LoginPage.FailAuthPopUp.notification_popup_text().text
        popup_existed_btn = LoginPage.FailAuthPopUp.notification_popup_btn().text
        with allure.step("Проверяем что текст попапа совпадает с ожидаемым"):
            assert_that(popup_existed_text, equal_to(popup_text))
        with allure.step("Проверяем что текст на кнопке попапа совпадает с ожидаемым"):
            assert_that(popup_existed_btn, equal_to(btn_text))
