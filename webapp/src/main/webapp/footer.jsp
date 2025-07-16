<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib uri="/WEB-INF/struts-tiles.tld" prefix="tiles" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<!-- footer.jsp - Local WormBase-style footer -->
<br/>
<br/>
<br/>

<div class="body" align="center" style="clear:both">
    <!-- contact -->
    <c:if test="${pageName != 'contact'}">
        <div id="contactFormDivButton">
            <im:vspacer height="11" />
            <div class="contactButton">
                <a href="#" onclick="showContactForm();return false">
                    <b><fmt:message key="feedback.title"/></b>
                </a>
            </div>
        </div>
        <div id="contactFormDiv" style="display:none;">
            <im:vspacer height="11" />
            <tiles:get name="contactForm" />
        </div>
    </c:if>
    <br/>

<!-- WormBase-style footer (local HTML, external links/images OK) -->
<div id="wormbase-footer" style="color:#CCC; background:black; margin:0; overflow:auto; position:relative; clear:both; padding: 1.5em 1.5em 1em;">
    <div id="wormbase-footer-nav" style="position:relative;">

        <div class="wb-footer-column" style="float:left; display: inline-block; width:12em;">
            <div class="wb-footer-title" style="font-weight: bold; margin-bottom: 1em; white-space: nowrap; font-size:1.1em; color:#eee;">About</div>
            <ul style="list-style:none; margin-left:0; padding-left:0;">
                <li style="line-height:2em; font-size:0.9em; white-space:nowrap;"><span style="color:#eee;">Nematodes</span></li>
                <li><a href="https://www.wormbase.org/about/userguide/nomenclature" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Nomenclature</a></li>
            </ul>

            <ul style="list-style:none; margin-left:0; padding-left:0;">
                <li style="line-height:2em; font-size:0.9em; white-space:nowrap;"><span style="color:#eee;">WormBase</span></li>
                <li><a href="https://www.wormbase.org/about#0--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Mission</a></li>
                <li><a href="https://www.wormbase.org/about/advisory_board#01--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Advisory Board</a></li>
                <li><a href="https://www.wormbase.org/about/policies#1--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Privacy</a></li>
                <li><a href="https://www.wormbase.org/about/policies#0--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Acceptable Use</a></li>
                <li><a href="https://www.wormbase.org/about/policies#2--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Copyright</a></li>
                <li><a href="https://www.wormbase.org/about/release_schedule#01--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Release Schedule</a></li>
                <li><a href="https://www.wormbase.org/about/citing_wormbase#012--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">How to Cite</a></li>
                <li><a href="https://www.wormbase.org/about/acknowledgments#0--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Acknowledgments</a></li>
                <li><a href="https://www.wormbase.org/about/staff#01--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">WormBase Staff</a></li>
                <li><a href="http://legacy.wormbase.org/" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Legacy Site</a></li>
            </ul>
        </div>

        <div class="wb-footer-column" style="float:left; display: inline-block; width:12em;">
            <div class="wb-footer-title" style="font-weight: bold; margin-bottom: 1em; white-space: nowrap; font-size:1.1em; color:#eee;">Support</div>
            <ul style="list-style:none; margin-left:0; padding-left:0;">
                <li><a href="https://www.wormbase.org/about/userguide/submit_data#01--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Submit Data</a></li>
                <li><a href="mailto:help@wormbase.org" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Email</a></li>
                <li><a href="https://www.wormbase.org/about/Frequently_asked_questions" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">FAQ</a></li>
                <li><a href="https://www.wormbase.org/about/userguide" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">User Guide</a></li>
                <li><a href="https://www.wormbase.org/tools/webinar.cgi" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Webinar</a></li>
                <li><a href="https://www.youtube.com/user/WormBaseHD" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">WormBaseHD YouTube</a></li>
                <li><a href="mailto:help@wormbase.org" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Contact Help</a></li>
            </ul>
        </div>

        <div class="wb-footer-column" style="float:left; display: inline-block; width:12em;">
            <div class="wb-footer-title" style="font-weight: bold; margin-bottom: 1em; white-space: nowrap; font-size:1.1em; color:#eee;">Community</div>
            <ul style="list-style:none; margin-left:0; padding-left:0;">
                <li><a href="https://wiki.wormbase.org/index.php/WormBoard" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">WormBoard</a></li>
                <li><a href="http://www.wormbook.org/" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">WormBook</a></li>
                <li><a href="https://community.alliancegenome.org/c/model-organism-worms/7" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Forum</a></li>
                <li><a href="https://www.wormbase.org/resources/laboratory#012--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Worm Labs</a></li>
                <li><a href="http://blog.wormbase.org" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Blog</a></li>
                <li><a href="http://twitter.com/wormbase" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Twitter</a></li>
                <li><a href="https://www.wormbase.org/species/c_elegans#1--10" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Key Papers</a></li>
            </ul>

            <ul style="list-style:none; margin-left:0; padding-left:0;">
                <li style="line-height:2em; font-size:0.9em; white-space:nowrap;"><span style="color:#eee;">Friends</span></li>
                <li><a href="https://cgc.umn.edu/" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">CGC</a></li>
                <li><a href="http://www.wormatlas.org" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">WormAtlas</a></li>
                <li><a href="http://www.nematodes.org/" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Nematodes.org</a></li>
                <li><a href="http://www.ipm.ucdavis.edu/NEMABASE/" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">NEMABASE</a></li>
                <li><a href="http://nematode.net/" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Nematode.net</a></li>
                <li><a href="http://www.smid-db.org/" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">SMID-DB</a></li>
                <li><a href="https://www.wormwiring.org/" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">WormWiring</a></li>
            </ul>
        </div>

        <div class="wb-footer-column" style="float:left; display: inline-block; width:12em;">
            <div class="wb-footer-title" style="font-weight: bold; margin-bottom: 1em; white-space: nowrap; font-size:1.1em; color:#eee;">Developer</div>
            <ul style="list-style:none; margin-left:0; padding-left:0;">
                <li><a href="https://www.wormbase.org/about/userguide/for_developers" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Developer Documentation</a></li>
                <li><a href="https://www.wormbase.org/about/userguide/for_developers/api-rest" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">RESTful API</a></li>
                <li><a href="http://github.com/WormBase" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Code Repositories (Github)</a></li>
                <li><a href="https://www.wormbase.org/about/internal_documentation" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">Staff Documentation</a></li>
            </ul>
        </div>

        <div class="wb-footer-column" style="float:left; display: inline-block; width:12em;">
            <div class="wb-footer-title" style="font-weight: bold; margin-bottom: 1em; white-space: nowrap; font-size:1.1em; color:#eee;">Downloads</div>
            <ul style="list-style:none; margin-left:0; padding-left:0;">
                <li><a href="https://downloads.wormbase.org" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">HTTPS site</a></li>
            </ul>
        </div>

        <div class="wb-footer-column" style="float:left; display: inline-block; width:12em;">
            <div class="wb-footer-title" style="font-weight: bold; margin-bottom: 1em; white-space: nowrap; font-size:1.1em; color:#eee;">Tools</div>
            <ul style="list-style:none; margin-left:0; padding-left:0;">
                <li><a href="${WEB_PROPERTIES['project.sitePrefix']}" style="color:#6FA2D9; text-decoration:none; font-weight:bold;">WormMine</a></li>
                <li><a href="http://www.intermine.org" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">InterMine</a></li>
                <li><a href="http://www.flymine.org" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">FlyMine</a></li>
                <li><a href="http://www.mousemine.org" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">MouseMine</a></li>
                <li><a href="http://ratmine.mcw.edu/ratmine" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">RatMine</a></li>
                <li><a href="http://yeastmine.yeastgenome.org" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">YeastMine</a></li>
                <li><a href="http://www.zebrafishmine.org" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">ZebrafishMine</a></li>
                <li><a href="http://www.humanmine.org" target="_blank" style="color:#aaa; text-decoration:none;" onmouseover="this.style.color='#6FA2D9'" onmouseout="this.style.color='#aaa'">HumanMine</a></li>
            </ul>
        </div>

    </div>

    <br style="clear:all" />

    <div id="wormbase-footermeta" style="float:left;">
        <a href="mailto:help@wormbase.org" style="height:30px; width: 30px; overflow: hidden; float:right; margin-right: 10px; color:white; font-size:20px; text-decoration:none;">📧</a>
        <a href="http://twitter.com/wormbase" target="_blank" style="height:30px; width: 30px; overflow: hidden; float:right; margin-right: 10px; color:white; font-size:20px; text-decoration:none;">🐦</a>
        <a href="http://feeds.feedburner.com/wormbase" target="_blank" style="height:30px; width: 30px; overflow: hidden; float:right; margin-right: 10px; color:white; font-size:20px; text-decoration:none;">📰</a>
    </div>

    <div id="wormbase-footercredit" style="font-size:0.9em; line-height:1.4em;">
        <br style="clear:both" />
        <div style="margin-top: 0.5em;">
            <div style="display: inline-block; margin: 1em 2em 1em 0; vertical-align: middle;">
                <a href="https://www.alliancegenome.org/" target="_blank"><img width="200px" src="https://www.wormbase.org/img/agr_founding_member_badge.png" alt="Alliance of Genome Resources" /></a>
            </div>
            <div style="display: inline-block; margin: 1em 2em 1em 0; vertical-align: middle;">
                <a href="http://www.caltech.edu/" target="_blank"><img width="150px" src="https://www.wormbase.org/img/caltech_logo.png" alt="Caltech" /></a>
            </div>
            <div style="display: inline-block; margin: 1em 2em 1em 0; vertical-align: middle;">
                <a href="https://www.ebi.ac.uk/" target="_blank"><img width="200px" src="https://www.wormbase.org/img/embl_ebi_logo_white.svg" alt="European Bioinformatics Institute" /></a>
            </div>
            <div style="display: inline-block; margin: 1em 2em 1em 0; vertical-align: middle;">
                <a href="https://oicr.on.ca/" target="_blank"><img height="65px" src="https://www.wormbase.org/img/oicr_logo_white.png" alt="Ontario Institute for Cancer Research" /></a>
            </div>
            <div style="display: inline-block; margin: 1em 2em 1em 0; vertical-align: middle;">
                <a href="https://globalbiodata.org" target="_blank"><img height="65px" src="https://www.wormbase.org/img/global-core-biodata-resources.svg" alt="Member: Global Core Biodata Resources" /></a>
            </div>
        </div>
        <div style="max-width: 70%;">
            <span>
                WormBase is supported by grant #U24 HG002223 from the
                <a href="http://www.genome.gov/" target="_blank" style="color:#6FA2D9; text-decoration:none;">National Human Genome Research Institute</a>
            </span><br />
            <span>at the <a href="http://www.nih.gov/" target="_blank" style="color:#6FA2D9; text-decoration:none;">US National Institutes of Health</a>,
                the <a href="http://www.mrc.ac.uk/" target="_blank" style="color:#6FA2D9; text-decoration:none;">UK Medical Research Council</a> and the
                <a href="http://www.bbsrc.ac.uk/home/home.aspx" target="_blank" style="color:#6FA2D9; text-decoration:none;">UK Biotechnology and Biological Sciences Research Council</a>.<br />
                In 2022, WormBase was named a <a href="https://globalbiodata.org/scientific-activities/global-core-biodata-resources/" target="_blank" style="color:#6FA2D9; text-decoration:none;">Core Member</a> of the <a href="https://globalbiodata.org/" target="_blank" style="color:#6FA2D9; text-decoration:none;">Global Biodata Coalition</a>.
            </span>
        </div>
    </div>

</div>
<!-- End WormBase-style footer -->

<!-- InterMine powered section -->
<div id="promo-footer">
  <div class="powered-footer footer">
    <p>Powered by</p>
    <a target="new" href="http://intermine.org" title="InterMine">
      <img src="images/icons/intermine-footer-logo.png" alt="InterMine logo" />
    </a>
  </div>
    <div class="cite-footer footer">
      <strong>Cite us:</strong>
          <cite>${WEB_PROPERTIES['project.citation']}</cite>
    </div>
</div>

</div>
<!-- /footer.jsp -->
