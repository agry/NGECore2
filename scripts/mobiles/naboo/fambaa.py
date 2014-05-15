import sys
from services.spawn import MobileTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	add.attack('bm_dampen_pain_2')
	add.attack('bm_shaken_2')
	add.attack('bm_stomp_2')
	mobileTemplates.setAttacks(attacks)
	templates = Vector()
	templates.add('object/mobile/shared_fambaa.iff')
	mobileTemplate.setCreatureName('fambaa')
	mobileTemplate.setTemplates(templates)
	mobileTemplate.setLevel(23)
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	core.spawnService.addMobileTemplate('fambaa', mobileTemplate)
	