"""
LinkedinController module for scrapping
"""
from selenium import webdriver
from . import SeleniumHelper


class LinkedinController(SeleniumHelper):
    TIMEOUT = 7
    data = {}

    SECTIONS = dict()
    FIELDS = dict()
    CONTAINER = dict()

    CONTAINER['CONTENT'] = '#profile'
    SECTIONS['CONTENT'] = dict()
    FIELDS['CONTENT'] = dict()

    # Profile Section: Basic information
    SECTIONS['CONTENT']['NAME'] = {'selector': '#name', 'type': 'text',
                                   'quantity': 'single'}
    SECTIONS['CONTENT']['IMAGE'] = {'selector': '.image.photo', 'type': 'attr',
                                    'attr': 'src', 'quantity': 'single'}
    SECTIONS['CONTENT']['CONNECTIONS'] = {'selector': '.member-connections',
                                          'type': 'text', 'quantity': 'single'}
    SECTIONS['CONTENT']['TITLE'] = {'selector': 'p.title', 'type': 'text',
                                    'quantity': 'single'}
    SECTIONS['CONTENT']['LOCATION'] = {'selector': '.locality',
                                       'type': 'text',
                                       'quantity': 'single'}
    SECTIONS['CONTENT']['INDUSTRY'] = {'selector': '#demographics '
                                                   'dd.descriptor:nth-child(2)',
                                       'type': 'text',
                                       'quantity': 'single'}
    SECTIONS['CONTENT']['RECOMMENDATIONS_NUMBER'] = {
        'selector': '.extra-info > tbody:nth-child(1) > tr:nth-child(4) > '
                    'td:nth-child(2) > strong:nth-child(1)',
        'type': 'text',
        'quantity': 'single'
    }

    # Profile Section: Summary
    SECTIONS['CONTENT']['SUMMARY'] = {'selector': '#summary .description',
                                      'type': 'text', 'quantity': 'single'}

    # Profile Section: Brief current
    SECTIONS['CONTENT']['BRIEF_CURRENT'] = {
        'selector': '[data-section="currentPositionDetails"] li',
        'quantity': 'multiple'
    }
    FIELDS['CONTENT']['BRIEF_CURRENT'] = dict()
    FIELDS['CONTENT']['BRIEF_CURRENT']['NAME'] = {'selector': 'a',
                                                  'type': 'text'}
    FIELDS['CONTENT']['BRIEF_CURRENT']['URL'] = {'selector': 'a',
                                                 'type': 'attr',
                                                 'attr': 'href'}

    # Profile Section: Brief previous
    SECTIONS['CONTENT']['BRIEF_PREVIOUS'] = {
        'selector': '[data-section="pastPositionDetails"] li',
        'quantity': 'multiple'
    }
    FIELDS['CONTENT']['BRIEF_PREVIOUS'] = dict()
    FIELDS['CONTENT']['BRIEF_PREVIOUS']['NAME'] = {'selector': 'a',
                                                   'type': 'text'}
    FIELDS['CONTENT']['BRIEF_PREVIOUS']['URL'] = {'selector': 'a',
                                                  'type': 'attr',
                                                  'attr': 'href'}

    # Profile Section: Brief education
    SECTIONS['CONTENT']['BRIEF_EDUCATION'] = {
        'selector': '[data-section="educationDetails"] li',
        'quantity': 'multiple'
    }
    FIELDS['CONTENT']['BRIEF_EDUCATION'] = dict()
    FIELDS['CONTENT']['BRIEF_EDUCATION']['NAME'] = {'selector': 'a',
                                                    'type': 'text'}
    FIELDS['CONTENT']['BRIEF_EDUCATION']['URL'] = {'selector': 'a',
                                                   'type': 'attr',
                                                   'attr': 'href'}

    # Profile Section: Websites
    SECTIONS['CONTENT']['WEBSITES'] = {
        'selector': '[data-section="websites"] li',
        'quantity': 'multiple'
    }
    FIELDS['CONTENT']['WEBSITES'] = dict()
    FIELDS['CONTENT']['WEBSITES']['NAME'] = {'selector': 'a', 'type': 'text'}
    FIELDS['CONTENT']['WEBSITES']['URL'] = {'selector': 'a', 'type': 'attr',
                                            'attr': 'href'}

    # Profile Section: Posts
    SECTIONS['CONTENT']['POSTS'] = {'selector': '.post',
                                    'quantity': 'multiple'}
    FIELDS['CONTENT']['POSTS'] = dict()
    FIELDS['CONTENT']['POSTS']['NAME'] = {'selector': '.item-title',
                                          'type': 'text'}
    FIELDS['CONTENT']['POSTS']['URL'] = {'selector': '.item-title a',
                                         'type': 'attr',
                                         'attr': 'href'}
    FIELDS['CONTENT']['POSTS']['IMG'] = {'selector': 'img',
                                         'type': 'attr',
                                         'attr': 'src'}
    FIELDS['CONTENT']['POSTS']['DATE'] = {'selector': '.time',
                                          'type': 'text'}

    # Profile Section: Experience
    SECTIONS['CONTENT']['EXPERIENCE'] = {'selector': '.position',
                                         'quantity': 'multiple'}
    FIELDS['CONTENT']['EXPERIENCE'] = dict()
    FIELDS['CONTENT']['EXPERIENCE']['TITLE'] = {'selector': '.item-title',
                                                'type': 'text'}
    FIELDS['CONTENT']['EXPERIENCE']['TITLE_URL'] = {'selector': '.item-title a',
                                                    'type': 'text',
                                                    'attr': 'href'}
    FIELDS['CONTENT']['EXPERIENCE']['IMG'] = {'selector': '.logo img',
                                              'type': 'attr',
                                              'attr': 'src'}
    FIELDS['CONTENT']['EXPERIENCE']['COMPANY'] = {
        'selector': '.item-subtitle a', 'type': 'text'}
    FIELDS['CONTENT']['EXPERIENCE']['COMPANY_URL'] = {
        'selector': '.item-subtitle a', 'type': 'attr', 'attr': 'href'
    }
    FIELDS['CONTENT']['EXPERIENCE']['DATE'] = {'selector': '.date-range',
                                               'type': 'text'}
    FIELDS['CONTENT']['EXPERIENCE']['DESCRIPTION'] = {
        'selector': '.description', 'type': 'text'
    }

    # Profile Section: Volunteer positions
    SECTIONS['CONTENT']['VOLUNTEER_POSITION'] = {
        'selector': '#volunteering .position', 'quantity': 'multiple'
    }
    FIELDS['CONTENT']['VOLUNTEER_POSITION'] = dict()
    FIELDS['CONTENT']['VOLUNTEER_POSITION']['TITLE'] = {
        'selector': '.item-title', 'type': 'text'
    }
    FIELDS['CONTENT']['VOLUNTEER_POSITION']['COMPANY'] = {
        'selector': '.item-subtitle', 'type': 'text'
    }
    FIELDS['CONTENT']['VOLUNTEER_POSITION']['DATE'] = {
        'selector': '.date-range', 'type': 'text'
    }
    FIELDS['CONTENT']['VOLUNTEER_POSITION']['CAUSE'] = {
        'selector': '.cause', 'type': 'text'
    }
    FIELDS['CONTENT']['VOLUNTEER_POSITION']['DESCRIPTION'] = {
        'selector': '.description', 'type': 'text'
    }

    # Profile Section: Volunteer opportunities
    SECTIONS['CONTENT']['VOLUNTEER_OPPORTUNITIES'] = {
        'selector': '#volunteering div.opportunities.extra-section li',
        'quantity': 'multiple'
    }
    FIELDS['CONTENT']['VOLUNTEER_OPPORTUNITIES'] = dict()
    FIELDS['CONTENT']['VOLUNTEER_OPPORTUNITIES']['NAME'] = {'selector': '',
                                                            'type': 'text'}

    # Profile Section: Volunteer causes
    SECTIONS['CONTENT']['VOLUNTEER_CAUSES'] = {
        'selector': '#volunteering div.extra-section.nth-child(3) > '
                    'ul:nth-child(2) > li',
        'quantity': 'multiple'
    }
    FIELDS['CONTENT']['VOLUNTEER_CAUSES'] = dict()
    FIELDS['CONTENT']['VOLUNTEER_CAUSES']['NAME'] = {'selector': '',
                                                     'type': 'text'}

    # Profile Section: Volunteer support
    SECTIONS['CONTENT']['VOLUNTEER_SUPPORT'] = {
        'selector': '#volunteering div.extra-section:nth-child(3) > '
                    'ul:nth-child(2) > li',
        'quantity': 'multiple'
    }
    FIELDS['CONTENT']['VOLUNTEER_SUPPORT'] = {}
    FIELDS['CONTENT']['VOLUNTEER_SUPPORT']['NAME'] = {'selector': '',
                                                      'type': 'text'}

    # Profile Section: Publication
    SECTIONS['CONTENT']['PUBLICATIONS'] = {'selector': '.publication',
                                           'quantity': 'multiple'}
    FIELDS['CONTENT']['PUBLICATIONS'] = {}
    FIELDS['CONTENT']['PUBLICATIONS']['NAME'] = {'selector': '.item-title',
                                                 'type': 'text'}
    FIELDS['CONTENT']['PUBLICATIONS']['URL'] = {'selector': '.item-title a',
                                                'type': 'attr', 'attr': 'href'}
    FIELDS['CONTENT']['PUBLICATIONS']['PLACE'] = {'selector': '.item-subtitle',
                                                  'type': 'text'}
    FIELDS['CONTENT']['PUBLICATIONS']['DATE'] = {'selector': '.date-range',
                                                 'type': 'text'}
    FIELDS['CONTENT']['PUBLICATIONS']['DESCRIPTION'] = {
        'selector': '.description', 'type': 'text'
    }
    FIELDS['CONTENT']['PUBLICATIONS']['CONTRIBUTORS'] = {
        'selector': '.contributors', 'type': 'text'}

    # Profile Section: Courses
    SECTIONS['CONTENT']['COURSES'] = {'selector': '.course',
                                      'quantity': 'multiple'}
    FIELDS['CONTENT']['COURSES'] = {}
    FIELDS['CONTENT']['COURSES']['NAME'] = {'selector': '', 'type': 'text'}

    # Profile Section: Projects
    SECTIONS['CONTENT']['PROJECTS'] = {'selector': '.project',
                                       'quantity': 'multiple'}
    FIELDS['CONTENT']['PROJECTS'] = {}
    FIELDS['CONTENT']['PROJECTS']['NAME'] = {'selector': '.item-title',
                                             'type': 'text'}
    FIELDS['CONTENT']['PROJECTS']['URL'] = {'selector': '.item-title a',
                                            'type': 'attr', 'attr': 'href'}
    FIELDS['CONTENT']['PROJECTS']['DATE'] = {'selector': '.date-range',
                                             'type': 'text'}
    FIELDS['CONTENT']['PROJECTS']['DESCRIPTION'] = {'selector': '.description',
                                                    'type': 'text'}
    FIELDS['CONTENT']['PROJECTS']['CONTRIBUTORS'] = {'selector': '.contributors',
                                                     'type': 'text'}

    # Profile Section: Awards
    SECTIONS['CONTENT']['AWARDS'] = {'selector': '.award',
                                     'quantity': 'multiple'}
    FIELDS['CONTENT']['AWARDS'] = {}
    FIELDS['CONTENT']['AWARDS']['NAME'] = {'selector': '.item-title',
                                           'type': 'text'}
    FIELDS['CONTENT']['AWARDS']['COMPANY'] = {'selector': '.item-subtitle',
                                              'type': 'text'}
    FIELDS['CONTENT']['AWARDS']['DATE'] = {'selector': '.date-range',
                                           'type': 'text'}
    FIELDS['CONTENT']['AWARDS']['DESCRIPTION'] = {'selector': '.description',
                                                  'type': 'text'}

    # Profile Section: Languages
    SECTIONS['CONTENT']['LANGUAGES'] = {'selector': '.language',
                                        'quantity': 'multiple'}
    FIELDS['CONTENT']['LANGUAGES'] = {}
    FIELDS['CONTENT']['LANGUAGES']['NAME'] = {'selector': '.name',
                                              'type': 'text'}
    FIELDS['CONTENT']['LANGUAGES']['LEVEL'] = {'selector': '.proficiency',
                                               'type': 'text'}

    # Profile Section: Skills
    SECTIONS['CONTENT']['SKILLS'] = {'selector': '.skill',
                                     'quantity': 'multiple'}
    FIELDS['CONTENT']['SKILLS'] = {}
    FIELDS['CONTENT']['SKILLS']['NAME'] = {'selector': 'a', 'type': 'text'}
    FIELDS['CONTENT']['SKILLS']['URL'] = {'selector': 'a', 'type': 'attr',
                                          'attr': 'href'}

    # Profile Section: Education
    SECTIONS['CONTENT']['EDUCATION'] = {'selector': '.school',
                                        'quantity': 'multiple'}
    FIELDS['CONTENT']['EDUCATION'] = {}
    FIELDS['CONTENT']['EDUCATION']['NAME'] = {'selector': '.item-title',
                                              'type': 'text'}
    FIELDS['CONTENT']['EDUCATION']['URL'] = {'selector': '.item-title a',
                                             'type': 'attr', 'attr': 'href'}
    FIELDS['CONTENT']['EDUCATION']['DEGREE'] = {'selector': '.item-subtitle',
                                                'type': 'text'}
    FIELDS['CONTENT']['EDUCATION']['DATE'] = {'selector': '.date-range',
                                              'type': 'text'}
    FIELDS['CONTENT']['EDUCATION']['DESCRIPTION'] = {'selector': '.description',
                                                     'type': 'text'}
    FIELDS['CONTENT']['EDUCATION']['IMG'] = {'selector': '.logo img',
                                             'type': 'attr', 'attr': 'src'}

    # Profile Section: Interests
    SECTIONS['CONTENT']['INTERESTS'] = {'selector': '.interest',
                                        'quantity': 'multiple'}
    FIELDS['CONTENT']['INTERESTS'] = {}
    FIELDS['CONTENT']['INTERESTS']['NAME'] = {'selector': 'a', 'type': 'text'}
    FIELDS['CONTENT']['INTERESTS']['URL'] = {'selector': 'a', 'type': 'attr',
                                             'attr': 'href'}

    # Profile Section: Certifications
    SECTIONS['CONTENT']['CERTIFICATIONS'] = {'selector': '.certification',
                                             'quantity': 'multiple'}
    FIELDS['CONTENT']['CERTIFICATIONS'] = {}
    FIELDS['CONTENT']['CERTIFICATIONS']['NAME'] = {'selector': '.item-title',
                                                   'type': 'text'}
    FIELDS['CONTENT']['CERTIFICATIONS']['URL'] = {'selector': '.item-title a',
                                                  'type': 'attr', 'attr': 'href'}
    FIELDS['CONTENT']['CERTIFICATIONS']['DEGREE'] = {
        'selector': '.item-subtitle', 'type': 'text'
    }
    FIELDS['CONTENT']['CERTIFICATIONS']['DATE'] = {'selector': '.date-range',
                                                   'type': 'text'}
    FIELDS['CONTENT']['CERTIFICATIONS']['IMG'] = {'selector': '.logo img',
                                                  'type': 'attr', 'attr': 'src'}

    # Profile Section: Organizations
    SECTIONS['CONTENT']['ORGANIZATIONS'] = {'selector': '#organizations li',
                                            'quantity': 'multiple'}
    FIELDS['CONTENT']['ORGANIZATIONS'] = {}
    FIELDS['CONTENT']['ORGANIZATIONS']['NAME'] = {'selector': '.item-title',
                                                  'type': 'text'}
    FIELDS['CONTENT']['ORGANIZATIONS']['URL'] = {'selector': '.item-title a',
                                                 'type': 'attr', 'attr': 'href'}
    FIELDS['CONTENT']['ORGANIZATIONS']['DEGREE'] = {'selector': '.item-subtitle',
                                                    'type': 'text'}
    FIELDS['CONTENT']['ORGANIZATIONS']['DATE'] = {'selector': '.date-range',
                                                  'type': 'text'}

    # Profile Section: Patents
    SECTIONS['CONTENT']['PATENTS'] = {'selector': '.patent',
                                      'quantity': 'multiple'}
    FIELDS['CONTENT']['PATENTS'] = {}
    FIELDS['CONTENT']['PATENTS']['NAME'] = {'selector': '.item-title',
                                            'type': 'text'}
    FIELDS['CONTENT']['PATENTS']['URL'] = {'selector': '.item-title a',
                                           'type': 'attr', 'attr': 'href'}
    FIELDS['CONTENT']['PATENTS']['PLACE'] = {'selector': '.item-subtitle',
                                             'type': 'text'}
    FIELDS['CONTENT']['PATENTS']['DESCRIPTION'] = {'selector': '.description',
                                                   'type': 'text'}
    FIELDS['CONTENT']['PATENTS']['CONTRIBUTORS'] = {'selector': '.contributors',
                                                    'type': 'text'}

    # Profile Section: Scores
    SECTIONS['CONTENT']['SCORES'] = {'selector': '.score',
                                     'quantity': 'multiple'}
    FIELDS['CONTENT']['SCORES'] = {}
    FIELDS['CONTENT']['SCORES']['NAME'] = {'selector': '.item-title',
                                           'type': 'text'}
    FIELDS['CONTENT']['SCORES']['VALUE'] = {'selector': '.item-subtitle',
                                            'type': 'text'}
    FIELDS['CONTENT']['SCORES']['DATE'] = {'selector': '.date-range',
                                           'type': 'text'}
    FIELDS['CONTENT']['SCORES']['DESCRIPTION'] = {'selector': '.description',
                                                  'type': 'text'}

    # Profile Section: Recommendations
    SECTIONS['CONTENT']['RECOMMENDATIONS'] = {'selector': '.recommendation',
                                              'quantity': 'multiple'}
    FIELDS['CONTENT']['RECOMMENDATIONS'] = {}
    FIELDS['CONTENT']['RECOMMENDATIONS']['NAME'] = {'selector': '',
                                                    'type': 'text'}

    # Profile Section: Groups
    SECTIONS['CONTENT']['GROUPS'] = {'selector': '.group',
                                     'quantity': 'multiple'}
    FIELDS['CONTENT']['GROUPS'] = {}
    FIELDS['CONTENT']['GROUPS']['NAME'] = {'selector': '.item-title',
                                           'type': 'text'}
    FIELDS['CONTENT']['GROUPS']['URL'] = {'selector': '.item-title a',
                                          'type': 'attr', 'attr': 'href'}
    FIELDS['CONTENT']['GROUPS']['IMG'] = {'selector': '.logo img',
                                          'type': 'attr',
                                          'attr': 'src'}
    # Profile Section: Related
    SECTIONS['CONTENT']['RELATED'] = {'selector': '.profile-card',
                                      'quantity': 'multiple'}
    FIELDS['CONTENT']['RELATED'] = {}
    FIELDS['CONTENT']['RELATED']['NAME'] = {'selector': '.item-title',
                                            'type': 'text'}
    FIELDS['CONTENT']['RELATED']['URL'] = {'selector': '.item-title a',
                                           'type': 'attr', 'attr': 'href'}
    FIELDS['CONTENT']['RELATED']['VALUE'] = {'selector': '.headline',
                                             'type': 'text'}
    FIELDS['CONTENT']['RELATED']['IMG'] = {'selector': 'img', 'type': 'attr',
                                           'attr': 'src'}

    def perform_clicks(self):
        self.click_selector('.skill.see-more')
        self.click_selector('.interest.see-more')
        self.click_selector('.group.see-more')

    def extract_profile(self, url):
        self.load_and_wait(url, self.CONTAINER['CONTENT'])
        self.perform_clicks()
        self.data = self.extract_profile('CONTENT')
        return self.data

    def is_profile_valid(self):
        return self.SECTIONS['CONTENT']['NAME'] is not None

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_page_load_timeout(self.TIMEOUT)
